import { useState } from "react";
import { loginUser } from "../api";

export default function Login({ setPage }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    const data = await loginUser(email, password);

    if (data.access_token) {
      localStorage.setItem("token", data.access_token);
      window.location.reload();
    } else {
      alert(data.detail || "Login failed");
    }
  };

  return (
    <div>
      <h2>Login</h2>

      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />

      <button onClick={handleLogin}>Login</button>

      <p onClick={() => setPage("register")}>Register</p>
    </div>
  );
}