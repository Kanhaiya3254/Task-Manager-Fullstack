import { useState } from "react";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";

export default function App() {
  const [page, setPage] = useState("login");

  const token = localStorage.getItem("token");

  if (token) {
    return <Dashboard setPage={setPage} />;
  }

  return (
    <div>
      {page === "login" && <Login setPage={setPage} />}
      {page === "register" && <Register setPage={setPage} />}
    </div>
  );
}