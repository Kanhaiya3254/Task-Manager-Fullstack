# 🚀 Task Manager Fullstack App

A full-stack Task Manager application built using **React (Frontend)** and **FastAPI (Backend)** with **JWT Authentication**.
This project allows users to securely manage their daily tasks with complete CRUD functionality.

---

## 📌 Features

* 🔐 User Authentication (Register & Login using JWT)
* ➕ Create Tasks
* 📋 View Tasks
* ✏️ Update Tasks
* ❌ Delete Tasks
* 🚪 Logout Functionality
* 🔒 Protected Routes (Only logged-in users can access tasks)

---

## 🛠️ Tech Stack

### 🔹 Frontend

* React.js
* JavaScript
* HTML & CSS

### 🔹 Backend

* FastAPI
* Python
* SQLAlchemy
* SQLite

### 🔹 Authentication

* JWT (JSON Web Token)

---

## 📂 Project Structure

```
task-manager-fullstack/
│
├── backend/
│   ├── app/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── routes/
│   │   ├── auth.py
│   │   ├── database.py
│   │   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.js
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository

```bash
git clone https://github.com/your-username/task-manager-fullstack.git
cd task-manager-fullstack
```

---

### 🔹 2. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)

pip install -r requirements.txt

uvicorn app.main:app --reload
```

👉 Backend runs on:
`http://127.0.0.1:8000`

---

### 🔹 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

👉 Frontend runs on:
`http://localhost:3000`

---

## 🔑 API Endpoints

| Method | Endpoint    | Description   |
| ------ | ----------- | ------------- |
| POST   | /register   | Register user |
| POST   | /login      | Login user    |
| GET    | /tasks      | Get all tasks |
| POST   | /tasks      | Create task   |
| PUT    | /tasks/{id} | Update task   |
| DELETE | /tasks/{id} | Delete task   |

---

## 🧠 Learning Outcomes

Through this project, I learned:

* Building REST APIs using FastAPI
* Implementing JWT Authentication
* Connecting frontend with backend
* Managing state in React
* Handling real-world bugs and debugging
* Full-stack application development

---

## ⚠️ Challenges Faced

* Fixing API errors (500 Internal Server Error)
* Handling JWT token authentication
* Debugging frontend-backend integration issues
* Managing user-specific data securely

---

## 📸 Screenshots

*(Add your screenshots here)*

---

## 🚀 Future Improvements

* Add task priority & status
* UI improvements (better design)
* Deploy on cloud (Render / Vercel)
* Add due dates & notifications

---

## 👨‍💻 Author

**Kanhaiya Kumar**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
