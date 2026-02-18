import { useState, useRef, useEffect } from "react";
import { sendChatMessage } from "./api/chat";
import "./App.css";

interface Message {
  role: "user" | "bot";
  text: string;
}

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const handleSend = async () => {
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { role: "user", text: input }]);
    setInput("");
    setLoading(true);

    try {
      const res = await sendChatMessage(input);
      setMessages((prev) => [...prev, { role: "bot", text: res.answer }]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "❌ Backend not responding" },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="chat-app">
      <h2 className="title">CrowdSenseNeo</h2>

      <div className="chat-box">
        {messages.map((m, i) => (
          <div key={i} className={`message ${m.role}`}>
            {m.text}
          </div>
        ))}
        {loading && <div className="message bot">🤖 typing...</div>}
        <div ref={bottomRef} />
      </div>

      <div className="input-box">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          placeholder="Ask about crowd safety..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default App;