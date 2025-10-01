# Library Management System

This is a small project where I’m building a **Library Management System** step by step. It starts as a simple CRUD API to manage books, and I’ll expand it over time with a database, user accounts, authentication, and eventually a frontend. The goal is to learn backend and full-stack development gradually, committing improvements along the way.

---

## Features (Phase 1)

* Add a new book (title, author, year, description)
* List all books
* View a single book by ID
* Update a book
* Delete a book

> Currently uses in-memory storage. Later versions will include a database for persistence.

---

## Tech Stack

* **FastAPI** – web framework for building APIs
* **Pydantic** – for request/response models
* **Uvicorn** – ASGI server to run FastAPI

> No database yet; in-memory storage is used for simplicity in the first phase.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ParsaNaderiX/library-management-system.git
cd library-management-system
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

* Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see the interactive API docs.
* You can test all CRUD operations directly from the Swagger interface.

---

## Project Structure

```
library-management-system/
│── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI entrypoint
│   ├── models.py        # Pydantic models for books
│   └── crud.py          # CRUD functions for in-memory storage
│
│── requirements.txt
│── .gitignore
│── README.md
```

---

## Project Roadmap

* **Phase 1:** Basic CRUD (with in-memory storage) -> Done!
* **Phase 2:** Database integration
* **Phase 3:** User accounts & authentication
* **Phase 4:** Advanced features: search, filtering, pagination
* **Phase 5:** Frontend interface
* **Phase 6:** Production setup: Docker, deployment

> Each phase will be committed separately, so the GitHub history shows my learning process.
