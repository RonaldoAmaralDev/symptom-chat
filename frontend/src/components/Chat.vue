<template>
  <div class="chat">
    <!-- Top bar -->
    <header class="chat-header">
      <h2>💬 Chat</h2>
      <button class="reset" @click="resetSession">🗑 Resetar conversa</button>
    </header>

    <!-- Histórico -->
    <main class="chat-history" ref="scroller">
      <div
        v-for="(m, i) in messages"
        :key="i"
        class="msg"
        :class="m.role === 'user' ? 'right' : 'left'"
      >
        <div class="bubble">
          <div class="role">{{ m.role === 'user' ? 'Você' : 'Assistente' }}</div>
          <div class="content">{{ m.content }}</div>
        </div>
      </div>

      <div v-if="loading" class="status">Gerando resposta…</div>
      <div v-if="error" class="error">Erro: {{ error }}</div>
    </main>

    <!-- Input -->
    <footer class="chat-input">
      <input
        v-model="input"
        @keyup.enter="send"
        type="text"
        placeholder="Descreva seus sintomas…"
      />
      <button :disabled="!input || loading" @click="send">Enviar</button>
    </footer>
  </div>
</template>

<script setup>
import { ref, nextTick } from "vue";
import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8088";

const messages = ref([]);
const input = ref("");
const loading = ref(false);
const error = ref("");
const scroller = ref(null);

const sessionId = "demo-1";

const scrollToBottom = async () => {
  await nextTick();
  if (scroller.value) scroller.value.scrollTop = scroller.value.scrollHeight;
};

const send = async () => {
  if (!input.value || loading.value) return;
  const userText = input.value.trim();
  input.value = "";
  messages.value.push({ role: "user", content: userText });
  scrollToBottom();

  try {
    loading.value = true;
    const res = await axios.post(`${API_BASE}/chat`, {
      session_id: sessionId,
      message: userText,
    });

    messages.value.push({
      role: "assistant",
      content: res.data?.answer || "(sem resposta)",
    });
  } catch (e) {
    error.value = e?.response?.data?.detail || e?.message;
    messages.value.push({ role: "assistant", content: "Ops, erro ao responder." });
  } finally {
    loading.value = false;
    scrollToBottom();
  }
};

const resetSession = async () => {
  try {
    await axios.delete(`${API_BASE}/session/${sessionId}`);
  } catch (_) {}
  messages.value = [];
  error.value = "";
};
</script>
