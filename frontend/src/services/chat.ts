const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8088/api/v1";

export async function sendMessage(
  sessionId: string,
  userText: string,
  onChunk: (token: string) => void
) {
  const response = await fetch(`${API_BASE}/chat/stream`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sessionId, message: userText }),
  });

  if (!response.ok || !response.body) {
    throw new Error("Falha ao conectar ao stream do chat");
  }

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
          onChunk(token);
        }
      }
    });
  }
}

export async function resetChat(sessionId: string): Promise<void> {
  await fetch(`${API_BASE}/session/${sessionId}`, { method: "DELETE" });
}

export async function getSession(sessionId: string): Promise<any> {
  const response = await fetch(`${API_BASE}/session/${sessionId}`);
  if (!response.ok) {
    throw new Error("Erro ao carregar sessão");
  }
  return await response.json();
}
