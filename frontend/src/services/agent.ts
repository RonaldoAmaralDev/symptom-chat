import api from "./http";

export interface Agent {
  id: number;
  name: string;
  provider: string;
  enabled: boolean;
  api_key?: string | null;
  config?: Record<string, any> | null;
  logo_url?: string | null;
  created_at: string;
  updated_at: string;
}

export async function listAgents(): Promise<Agent[]> {
  const { data } = await api.get<Agent[]>("/agents");
  return data;
}

export async function toggleAgent(id: number) {
  const { data } = await api.put(`/agents/${id}/toggle`);
  return data;
}

export async function updateAgent(id: number, payload: Partial<Agent>) {
  const { data } = await api.put(`/agents/${id}`, payload);
  return data;
}