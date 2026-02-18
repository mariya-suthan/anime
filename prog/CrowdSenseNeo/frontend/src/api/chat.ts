export interface ChatRequest {
  query: string;
}

export interface ChatResponse {
  answer: string;
}

const API_URL = import.meta.env.VITE_API_URL;

export async function sendChatMessage(
  query: string
): Promise<ChatResponse> {
  const response = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  });

  if (!response.ok) {
    throw new Error("Backend error");
  }

  return response.json() as Promise<ChatResponse>;
}