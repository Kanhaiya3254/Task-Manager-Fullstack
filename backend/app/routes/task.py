from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, auth
from ..database import SessionLocal
from ..auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# ======================
# DB Dependency
# ======================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ======================
# GET ALL TASKS
# ======================
@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return db.query(models.Task).filter(
        models.Task.owner_id == current_user.id
    ).all()

# ======================
# CREATE TASK
# ======================
@router.post("/")
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    new_task = models.Task(
        title=task.title,
        description=task.description,
        owner_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# ======================
# UPDATE TASK
# ======================
@router.put("/{task_id}")
def update_task(
    task_id: int,
    updated_task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description

    db.commit()
    db.refresh(task)

    return {"message": "Task updated", "task": task}

# ======================
# DELETE TASK (FIXED)
# ======================
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    # 1️⃣ user fetch safely
    user = db.query(models.User).filter(
        models.User.email == current_user
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    # 2️⃣ task fetch
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # 3️⃣ delete safely
    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}