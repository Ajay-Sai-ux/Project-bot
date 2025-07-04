"use client";

import { useState } from "react";

export default function Dashboard() {
  const [symbol, setSymbol] = useState("");
  const [quantity, setQuantity] = useState("");
  const [side, setSide] = useState("BUY");
  const [status, setStatus] = useState(null);

  const placeOrder = async () => {
    try {
      const res = await fetch("http://localhost:8000/trade/place-order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          symbol,
          quantity: parseInt(quantity),
          transaction_type: side,
        }),
      });

      const data = await res.json();
      if (res.ok) {
        setStatus(`✅ ${side} order placed: ${data.order_id}`);
      } else {
        setStatus(`❌ Error: ${data.detail}`);
      }
    } catch (error) {
      setStatus("❌ Failed to place order");
    }
  };

  return (
    <main style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>📊 Trading Dashboard</h1>

      <div style={{ marginTop: "1rem" }}>
        <input
          placeholder="Symbol (e.g. INFY)"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value)}
          style={{ padding: "0.5rem", marginRight: "1rem" }}
        />

        <input
          placeholder="Quantity"
          type="number"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          style={{ padding: "0.5rem", marginRight: "1rem" }}
        />

        <select value={side} onChange={(e) => setSide(e.target.value)} style={{ padding: "0.5rem" }}>
          <option value="BUY">Buy</option>
          <option value="SELL">Sell</option>
        </select>

        <button
          onClick={placeOrder}
          style={{
            padding: "0.5rem 1rem",
            backgroundColor: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "6px",
            marginLeft: "1rem",
            cursor: "pointer",
          }}
        >
          Place Order
        </button>
      </div>

      {status && <p style={{ marginTop: "1rem" }}>{status}</p>}
    </main>
  );
}
