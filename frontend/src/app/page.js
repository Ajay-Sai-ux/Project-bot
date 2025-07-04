"use client";

import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  const handleLogin = () => {
    // Redirects to your FastAPI backend
    window.location.href = "http://localhost:8000/auth/login-url";
  };

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <Image
          className={styles.logo}
          src="/next.svg"
          alt="Next.js logo"
          width={180}
          height={38}
          priority
        />
        <p>API for Kite Connect integration.</p>

        <div className={styles.ctas}>
          <button onClick={handleLogin} className={styles.primary}>
            Login to Kite
          </button>
        </div>
      </main>
    </div>
  );
}
