from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


class TaskRequest(BaseModel):
    title: str
    completed: bool = False


# Keep data in memory while the application is running.
tasks: list[Task] = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks.
    return []


@app.post("/tasks")
def create_task(task_request: TaskRequest):
    # TODO: Create a task with a unique ID and return it.
    raise NotImplementedError


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Return the matching task or a 404 response.
    raise NotImplementedError


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_request: TaskRequest):
    # TODO: Update the matching task or return a 404 response.
    raise NotImplementedError


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete the matching task or return a 404 response.
    raise NotImplementedError
