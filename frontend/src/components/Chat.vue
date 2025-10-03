<template>
  <div class="chat">
    <header class="chat-header">
      <h2>💬 Chat</h2>
      <button class="reset" @click="resetSession">🗑 Limpar conversa</button>
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
import { ref, nextTick, onMounted, watchEffect } from "vue";
import { sendMessage, resetChat } from "@/services/chatService";
import { toast } from "vue3-toastify";
import { getSession } from "../services/chatService";

const messages = ref([]);
const input = ref("");
const loading = ref(false);
const scroller = ref(null);

const sessionId = "demo-1";

const scrollToBottom = async () => {
  await nextTick();
  setTimeout(() => {
    if (scroller.value) {
      scroller.value.scrollTop = scroller.value.scrollHeight;
    }
  }, 0);
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

  try {
    await sendMessage(sessionId, userText, (token) => {
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
    });
  } catch (e) {
    toast.error(e.message || "Erro inesperado 🚨");
    aiMsg.content = "❌ Ocorreu um erro ao gerar resposta.";
  } finally {
    loading.value = false;
    scrollToBottom();
  }
};

const resetSession = async () => {
  try {
    await resetChat(sessionId);
  } catch (_) {}
  messages.value = [];
};

onMounted(async () => {
  try {
    const history = await getSession(sessionId);
    messages.value = history.messages;

    await nextTick();
    scrollToBottom();
  } catch (e) {
    console.error("Erro ao carregar histórico:", e);
  }
});

watchEffect(async () => {
  await nextTick();
  scrollToBottom();
});
</script>
