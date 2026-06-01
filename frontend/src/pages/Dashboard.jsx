import { useEffect, useState } from "react";

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const token = localStorage.getItem("token");

  // ======================
  // LOGOUT
  // ======================
  const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  // ======================
  // FETCH TASKS
  // ======================
  const fetchTasks = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/tasks", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await res.json();
      setTasks(data);
    } catch (err) {
      console.log("Fetch error:", err);
    }
  };

  useEffect(() => {
    if (token) {
      fetchTasks();
    } else {
      window.location.href = "/login";
    }
  }, []);

  // ======================
  // ADD TASK
  // ======================
  const addTask = async () => {
    if (!title || !description) return alert("Fill all fields");

    const res = await fetch("http://127.0.0.1:8000/tasks", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ title, description }),
    });

    await res.json();

    setTitle("");
    setDescription("");
    fetchTasks();
  };

  // ======================
  // DELETE TASK
  // ======================
  const deleteTask = async (id) => {
    const res = await fetch(`http://127.0.0.1:8000/tasks/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    await res.json();
    fetchTasks();
  };

  return (
    <div style={{ padding: "20px" }}>
      
      {/* HEADER */}
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <h2>Dashboard</h2>

        {/* LOGOUT */}
        <button onClick={logout} style={{ background: "red", color: "white" }}>
          Logout
        </button>
      </div>

      {/* ADD TASK */}
      <div style={{ marginTop: "20px" }}>
        <input
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ marginRight: "10px" }}
        />

        <input
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          style={{ marginRight: "10px" }}
        />

        <button onClick={addTask} style={{ background: "green", color: "white" }}>
          Add Task
        </button>
      </div>

      {/* TASK LIST */}
      <div style={{ marginTop: "30px" }}>
        <h3>Tasks</h3>

        {tasks.length === 0 ? (
          <p>No tasks found</p>
        ) : (
          tasks.map((task) => (
            <div
              key={task.id}
              style={{
                border: "1px solid #ccc",
                padding: "10px",
                marginTop: "10px",
              }}
            >
              <h4>{task.title}</h4>
              <p>{task.description}</p>

              {/* DELETE BUTTON */}
              <button
                onClick={() => deleteTask(task.id)}
                style={{ background: "red", color: "white" }}
              >
                Delete
              </button>
            </div>
          ))
        )}
      </div>
    </div>
  );
}