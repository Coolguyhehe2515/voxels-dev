"use client";

import { FormEvent, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendMessage(event: FormEvent) {
    event.preventDefault();

    if (!message.trim() || loading) return;

    setLoading(true);
    setResponse("");

    try {
      const result = await fetch("/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message
        })
      });

      const data = await result.json();

      if (!result.ok) {
        throw new Error(data.error || "Request failed.");
      }

      setResponse(data.response);
    } catch (error) {
      setResponse(
        error instanceof Error ? error.message : "Something went wrong."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main>
      <h1>voxeldev</h1>
      <p>AI-powered development workspace</p>

      <form onSubmit={sendMessage}>
        <textarea
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          placeholder="Ask voxeldev..."
          rows={6}
        />

        <button type="submit" disabled={loading}>
          {loading ? "Thinking..." : "Send"}
        </button>
      </form>

      {response && (
        <section>
          <h2>voxeldev</h2>
          <pre>{response}</pre>
        </section>
      )}
    </main>
  );
}
