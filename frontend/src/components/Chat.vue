<template>
  <div class="chat">
    <header class="chat-header">
      <h2>💬 Chat</h2>
      <button class="reset" @click="resetSession">🗑 Resetar conversa</button>
    </header>

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

      <div v-if="loading" class="status">✍️ Digitando…</div>
      <div v-if="error" class="error">Erro: {{ error }}</div>
    </main>

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

  const aiMsg = { role: "assistant", content: "" };
  messages.value.push(aiMsg);

  scrollToBottom();
  loading.value = true;
  error.value = "";

  try {
    const response = await fetch(`${API_BASE}/chat/stream`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: sessionId, message: userText }),
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value, { stream: true });
      chunk.split("\n\n").forEach((line) => {
        if (line.startsWith("data:")) {
          const token = line.replace("data:", "").trim();
      if (token) {
        if (
          aiMsg.content &&
          !aiMsg.content.endsWith(" ") &&
          !token.startsWith(" ") &&
          !",.!?".includes(token)
        ) {
          aiMsg.content += " ";
        }
        aiMsg.content += token;
        scrollToBottom();
      }
        }
      });
    }
  } catch (e) {
    error.value = e.message || "Erro inesperado.";
    aiMsg.content = "❌ Erro ao gerar resposta.";
  } finally {
    loading.value = false;
    scrollToBottom();
  }
};

const resetSession = async () => {
  try {
    await fetch(`${API_BASE}/session/${sessionId}`, { method: "DELETE" });
  } catch (_) {}
  messages.value = [];
  error.value = "";
};
</script>
