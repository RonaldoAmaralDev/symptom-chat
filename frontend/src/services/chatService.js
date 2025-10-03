const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8088";

export async function sendMessage(sessionId, userText, onChunk) {
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
          onChunk(token);
        }
      }
    });
  }
}

export async function resetChat(sessionId) {
  await fetch(`${API_BASE}/session/${sessionId}`, { method: "DELETE" });
}

export async function getSession(sessionId) {
  const response = await fetch(`${API_BASE}/session/${sessionId}`);
  if (!response.ok) {
    throw new Error("Erro ao carregar sessão");
  }
  return await response.json();
}