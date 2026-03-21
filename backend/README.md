Command to install dependencies:-
```
pip install "fastapi[standard]" sqlalchemy psycopg2-binary pydantic-settings python-dotenv
```

Project Backend Structure:-
```
farp-demo-proj/backend/
|
├── app/                        # Main application package
│   ├── __init__.py
│   ├── main.py                 # App entry point & initialization
│   ├── api/                    # API Route handlers (Endpoints)
│   │   ├── __init__.py
│   │   └── v1/                 # Versioning your API
│   │       ├── __init__.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── products.py # All product-related routes
│   ├── core/                   # Global configuration
│   │   ├── __init__.py
│   │   └── config.py           # Settings, .env loading
│   ├── db/                     # Database logic
│   │   ├── __init__.py
│   │   ├── session.py          # Formerly db_config.py
│   │   └── base_class.py       # Declarative Base
│   ├── models/                 # SQLAlchemy Models (Database tables)
│   │   ├── __init__.py
│   │   └── product.py          # Formerly db_models.py
│   └── schemas/                # Pydantic Schemas (Validation)
│       ├── __init__.py
│       └── product.py          # Formerly models.py
├── .env                        # Secret credentials
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt
```
