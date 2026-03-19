# FARP DEMO - ProdTrac: Professional FastAPI Product Management API

**ProdTrac** is a full-stack product management system built with a modern, decoupled architecture. It demonstrates how to build a scalable backend with FastAPI and SQLAlchemy 2.0, connected to a reactive frontend built with React.js.

-----

## Architecture

This project is split into two main directories to maintain a clean separation of concerns:

```text
ProdTrac/
├── backend/                # FastAPI + SQLAlchemy + Postgres
│   ├── app/
│   │   ├── api/v1/         # Versioned endpoints
│   │   ├── core/           # Pydantic Settings & Config
│   │   ├── db/             # Session & Base Class
│   │   ├── models/         # SQLAlchemy 2.0 Models
│   │   ├── schemas/        # Pydantic v2 Validation
│   │   └── main.py         # Entry point & CORS
│   └── .env                # Database secrets
└── frontend/               # React.js
    ├── src/                # Components & API hooks
    └── .env                # API Base URL configuration
```

-----

## Key Features

  - **Backend (FastAPI)**:
      - Fully typed CRUD operations.
      - SQLAlchemy 2.0 with `Mapped` types for better IDE support.
      - Automatic interactive documentation (Swagger/OpenAPI).
  - **Frontend (React)**:
      - Built with **Create React App (CRA)**.
      - Asynchronous data fetching from the FastAPI service.
      - Dynamic UI updates based on inventory changes.
  - **Database (Postgres)**:
      - Relational data storage with indexed lookups.
      - Connection pooling enabled for high-concurrency performance.

-----

## Installation & Setup

### 1\. Database Setup

Ensure you have a PostgreSQL instance running and create a database named `prodtrac_db`.

### 2\. Backend Setup (FastAPI)

```bash
cd backend
python -m venv .venv
# Activate: .venv\Scripts\activate (Win) or source .venv/bin/activate (Mac/Linux)
pip install -r requirements.txt
```

Create a `.env` file in `/backend`:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=prodtrac_db
```

**Run Backend:**

```bash
uvicorn app.main:app --reload
```

### 3\. Frontend Setup (React)

```bash
cd frontend
npm install
```

**Run Frontend:**

```bash
npm start
```

-----

## PI Documentation

With the backend running, you can access the auto-generated docs:

  - **Swagger UI**: [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
  - **ReDoc**: [http://localhost:8000/redoc](https://www.google.com/search?q=http://localhost:8000/redoc)

-----

## Built With

  - **FastAPI** - The high-performance Python framework.
  - **React.js** - For building the user interface.
  - **PostgreSQL** - The world's most advanced open-source database.
  - **SQLAlchemy 2.0** - Modern Python SQL Toolkit.
  - **Pydantic v2** - Data validation and settings management.
