from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, Base, SessionLocal
from . import models, schemas, auth

app = FastAPI()

# ======================
# CORS
# ======================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .routes import task

app.include_router(task.router)
# ======================
# CREATE TABLES (SAFE)
# ======================
Base.metadata.create_all(bind=engine)

# ======================
# DB SESSION
# ======================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ======================
# HOME
# ======================
@app.get("/")
def home():
    return {"message": "API running 🚀"}

# ======================
# REGISTER
# ======================
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = models.User(
        email=user.email,
        password=auth.hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}

# ======================
# LOGIN
# ======================
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    if not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Wrong password")

    token = auth.create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# ======================
# CREATE TASK
# ======================
@app.post("/tasks")
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):

    user = db.query(models.User).filter(
        models.User.email == current_user
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_task = models.Task(
        title=task.title,
        description=task.description,
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# ======================
# GET TASKS
# ======================
@app.get("/tasks")
def get_tasks(
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):

    user = db.query(models.User).filter(
        models.User.email == current_user
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    tasks = db.query(models.Task).filter(
        models.Task.user_id == user.id
    ).all()

    return tasks

# ======================
# UPDATE TASK
# ======================
@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    updated_task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):

    user = db.query(models.User).filter(
        models.User.email == current_user
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description

    db.commit()
    db.refresh(task)

    return {"message": "Task updated", "task": task}

# ======================
# DELETE TASK
# ======================
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):

    user = db.query(models.User).filter(
        models.User.email == current_user
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}