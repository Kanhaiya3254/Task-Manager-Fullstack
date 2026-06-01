import { useState } from "react";
import { registerUser } from "../api";

export default function Register({ setPage }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {
    const data = await registerUser(email, password);

    alert(data.message || data.error);
    setPage("login");
  };

  return (
    <div>
      <h2>Register</h2>

      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />

      <button onClick={handleRegister}>Register</button>

      <p onClick={() => setPage("login")}>Login</p>
    </div>
  );
}