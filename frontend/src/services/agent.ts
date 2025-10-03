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