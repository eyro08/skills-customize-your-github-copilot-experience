# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small task-management REST API with FastAPI to practice HTTP methods, URL routes, request and response data, Pydantic models, and in-memory data storage.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Use the starter code to create a FastAPI application that can be run locally and responds to a health-check request.

#### Requirements

Completed program should:

- Create a FastAPI application object.
- Provide a `GET /health` route.
- Return `{"status": "ok"}` from the health-check route.
- Run with Uvicorn using a command such as `uvicorn starter-code:app --reload`.

### 🛠️ Build the Task Collection Endpoints

#### Description

Represent tasks with a Pydantic model and implement routes for creating and listing tasks in an in-memory collection.

#### Requirements

Completed program should:

- Define a task model with an integer ID, a title, and a Boolean completion status.
- Provide a `GET /tasks` route that returns all stored tasks.
- Provide a `POST /tasks` route that accepts a task request and adds a new task.
- Assign each new task a unique integer ID.
- Return the created task from the `POST /tasks` route.

Example request:

```json
{
  "title": "Read about HTTP methods",
  "completed": false
}
```

### 🛠️ Add Single-Task Operations

#### Description

Add routes for retrieving, updating, and deleting one task by its ID, including a useful response when the task does not exist.

#### Requirements

Completed program should:

- Provide a `GET /tasks/{task_id}` route that returns one matching task.
- Provide a `PUT /tasks/{task_id}` route that updates a task's title and completion status.
- Provide a `DELETE /tasks/{task_id}` route that removes a task.
- Return HTTP status code `404` when a requested task ID does not exist.
- Return a clear response after a task is deleted.
