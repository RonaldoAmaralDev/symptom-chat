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
          <td>
            <img :src="agent.logo_url" alt="logo" class="agent-logo" />
          </td>
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
              @click="toggleAgent(agent)"
            >
              {{ agent.enabled ? "Desativar" : "Ativar" }}
            </button>
            <button class="btn btn-primary" @click="editAgent(agent)">
              Editar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { listAgents, type Agent } from "@/services/agent";
import { toast } from "vue3-toastify";

const agents = ref<Agent[]>([]);

onMounted(async () => {
  try {
    agents.value = await listAgents();
  } catch (error) {
    console.error("Erro ao carregar agentes:", error);
  }
});

function toggleAgent(agent: Agent) {
  agent.enabled = !agent.enabled;
  toast.success('Status atualizado com sucesso!');
}

function editAgent(agent: Agent) {
  console.log("Editar agente:", agent);
}
</script>
