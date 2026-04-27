from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from model.todo_model import Todo
from config.database import get_db
from pydantic import BaseModel
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

print("Database connected ✅:", DATABASE_URL.split("/")[-1])

app = FastAPI()


# ✅ Use Pydantic model for request/response validation
class CreateTodo(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False


# ✅ Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}


# ✅ Create todo route with try/except
@app.post("/todos/")
def create_todo(todo: CreateTodo, db: Session = Depends(get_db)):
        db_todo = Todo(
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            created_at=datetime.utcnow()
        )
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

# ✅ Read todos route
@app.get("/todos/")
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos

# ✅ Read todo by ID route
@app.get("/todos/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return {"error": "Todo not found"}
    return todo

# ✅ Update todo route
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: CreateTodo, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        return {"error": "Todo not found"}
    db_todo.title = todo.title
    db_todo.description = todo.description
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo

# ✅ Delete todo route
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        return {"error": "Todo not found"}
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}


