# FARP DEMO - ProdTrac: Professional FastAPI Product Management API

**ProdTrac** is a production-ready FastAPI application designed with a clean, modular architecture. It features full CRUD operations, PostgreSQL integration via SQLAlchemy 2.0, Pydantic v2 validation, and centralized environment configuration.

## 🏗️ Project Structure

The project follows the **Industry Standard Layout** to ensure scalability and prevent circular imports:

```text
backend/
├── app/
│   ├── api/                # Route handlers
│   │   └── v1/             # Versioned API (v1)
│   ├── core/               # Global config & security
│   ├── db/                 # Database session & base class
│   ├── models/             # SQLAlchemy database models
│   ├── schemas/            # Pydantic validation models
│   └── main.py             # App entry point & middleware
├── .env                    # Environment secrets (Local only)
├── .gitignore              # Git exclusion rules
└── requirements.txt        # Project dependencies
```

-----

## ✨ Features

  - **Standardized CRUD**: Create, Read, Update, and Delete products.
  - **Modern SQLAlchemy**: Uses SQLAlchemy 2.0 `Mapped` and `mapped_column` syntax.
  - **Environment Management**: Centralized settings via `pydantic-settings` and `.env` files.
  - **Data Validation**: Strict type checking and serialization using Pydantic v2.
  - **CORS Enabled**: Pre-configured for a React frontend on `localhost:3000`.
  - **Auto-Documentation**: Interactive Swagger UI and ReDoc.

-----

## 🛠️ Setup & Installation

### 1\. Clone & Navigate

```bash
git clone <your-repo-url>
cd backend
```

### 2\. Virtual Environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 3\. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4\. Configuration

Create a `.env` file in the `backend/` root:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=prodtrac_db
```

### 5\. Run the Application

```bash
uvicorn app.main:app --reload
```

-----

## 📖 API Documentation

Once the server is running, explore the interactive documentation:

  - **Swagger UI**: [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
  - **ReDoc**: [http://localhost:8000/redoc](https://www.google.com/search?q=http://localhost:8000/redoc)

### Core Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Health Check |
| `GET` | `/api/v1/products/` | List all products |
| `GET` | `/api/v1/products/{id}` | Get product details |
| `POST` | `/api/v1/products/` | Create a new product |
| `PUT` | `/api/v1/products/{id}` | Update product (Partial) |
| `DELETE` | `/api/v1/products/{id}` | Remove a product |

-----

## 🧪 Example API Calls

### Create a Product

```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/products/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Mechanical Keyboard",
  "description": "RGB Backlit, Brown Switches",
  "price": 89.99,
  "quantity": 50
}'
```

-----

## 🛠️ Built With

  - **FastAPI**: High-performance web framework.
  - **SQLAlchemy 2.0**: SQL Toolkit and Object Relational Mapper.
  - **Pydantic v2**: Data parsing and validation.
  - **PostgreSQL**: Production-grade relational database.

Would you like me to help you create a **`CONTRIBUTING.md`** file in case you want to share this project with other developers?
