<template>
  <div class="chat">
    <header class="chat-header">
      <h2>💬 Chat</h2>

      <div class="agent-select">
        <label for="agent">Agente:</label>
        <select v-model="selectedAgent" id="agent">
          <option disabled value="">-- escolha um agente --</option>
          <option v-for="a in activeAgents" :key="a.id" :value="a.id">
            {{ a.name }}
          </option>
        </select>
      </div>

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
        placeholder="Digite sua mensagem..."
      />
      <button :disabled="!input || loading || !selectedAgent" @click="send">
        Enviar
      </button>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick, onMounted, watchEffect } from "vue";
import { sendMessage, resetChat, getSession } from "@/services/chat";
import { listAgents, type Agent } from "@/services/agent";
import { toast } from "vue3-toastify";

const messages = ref<any[]>([]);
const input = ref("");
const loading = ref(false);
const scroller = ref<HTMLElement | null>(null);

const sessionId = "demo-1";

const activeAgents = ref<Agent[]>([]);
const selectedAgent = ref<number | "">("");
const scrollToBottom = async () => {
  await nextTick();
  setTimeout(() => {
    if (scroller.value) {
      scroller.value.scrollTop = scroller.value.scrollHeight;
    }
  }, 0);
};

const send = async () => {
  if (!input.value || loading.value || !selectedAgent.value) return;

  const userText = input.value.trim();
  input.value = "";
  messages.value.push({ role: "user", content: userText });

  const aiMsg = { role: "assistant", content: "" };
  messages.value.push(aiMsg);

  scrollToBottom();
  loading.value = true;

  try {
    await sendMessage(sessionId, userText, Number(selectedAgent.value), (token) => {
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
  } catch (e: any) {
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
    messages.value = history.messages || [];

    const allAgents = await listAgents();
    activeAgents.value = allAgents.filter((a) => a.enabled);

    await nextTick();
    scrollToBottom();
  } catch (e) {
    console.error("Erro ao carregar:", e);
  }
});

watchEffect(async () => {
  await nextTick();
  scrollToBottom();
});
</script>