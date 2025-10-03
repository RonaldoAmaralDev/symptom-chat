<template>
  <div class="agent-container">
    <h2 class="title">Agentes</h2>

    <table class="agent-table">
      <thead>
        <tr>
          <th>Logo</th>
          <th>Nome</th>
          <th>Provider</th>
          <th>Status</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="agent in agents" :key="agent.id">
          <td><img :src="agent.logo_url" alt="logo" class="agent-logo" /></td>
          <td>{{ agent.name }}</td>
          <td>{{ agent.provider }}</td>
          <td>
            <span
              class="status"
              :class="agent.enabled ? 'status-active' : 'status-inactive'"
            >
              {{ agent.enabled ? "Ativo" : "Inativo" }}
            </span>
          </td>
          <td>
            <button
              class="btn"
              :class="agent.enabled ? 'btn-danger' : 'btn-success'"
              @click="toggle(agent)"
            >
              {{ agent.enabled ? "Desativar" : "Ativar" }}
            </button>
            <button class="btn btn-primary" @click="openEdit(agent)">
              Editar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="showModal" class="modal-backdrop">
      <div class="modal">
        <h3>Editar Agente</h3>
        <form @submit.prevent="saveEdit">
          <label>Nome</label>
          <input v-model="editForm.name" type="text" />

          <label>Provider</label>
          <input v-model="editForm.provider" type="text" />

          <label>Logo URL</label>
          <input v-model="editForm.logo_url" type="text" />

          <label>API Key</label>
          <input v-model="editForm.api_key" type="text" />

          <label>
            <input type="checkbox" v-model="editForm.enabled" />
            Ativo
          </label>

          <div class="modal-actions">
            <button type="submit" class="btn btn-primary">Salvar</button>
            <button type="button" class="btn btn-danger" @click="closeModal">
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { listAgents, toggleAgent, updateAgent, type Agent } from "@/services/agent";
import { toast } from "vue3-toastify";

const agents = ref<Agent[]>([]);
const showModal = ref(false);
const editForm = ref<Partial<Agent>>({});
const editingId = ref<number | null>(null);

onMounted(async () => {
  agents.value = await listAgents();
});

async function toggle(agent: Agent) {
  const res = await toggleAgent(agent.id);
  agent.enabled = res.agent.enabled;
  toast.success('Agente atualizado com sucesso!')
}

function openEdit(agent: Agent) {
  editingId.value = agent.id;
  editForm.value = { ...agent };
  showModal.value = true;
}

function closeModal() {
  showModal.value = false;
  editForm.value = {};
  editingId.value = null;
}

async function saveEdit() {
  if (!editingId.value) return;
  const res = await updateAgent(editingId.value, editForm.value);
  const idx = agents.value.findIndex((a) => a.id === editingId.value);
  if (idx !== -1) agents.value[idx] = res.agent;
  closeModal();
  toast.success('Agente atualizado com sucesso!')
}
</script>
