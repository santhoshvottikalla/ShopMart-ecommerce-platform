# ShopMart

> Production-oriented e-commerce backend built with Python, FastAPI, SQLAlchemy, and PostgreSQL.

ShopMart is a scalable e-commerce backend developed using a layered architecture with clear separation between API handling, business logic, data access, and database persistence.

The project focuses on clean architecture, secure authentication, database integrity, maintainability, and production-oriented backend engineering.

---

## 🚧 Project Status

**Current Version:** `0.x` — Backend Foundation + Authentication

### ✅ Implemented

- FastAPI REST API
- PostgreSQL integration
- SQLAlchemy ORM
- Layered architecture
- Repository and Service layers
- Pydantic validation
- Dependency injection
- Product CRUD APIs
- Category CRUD APIs
- User registration and login
- bcrypt password hashing
- JWT authentication
- Bearer token authentication
- Authenticated user endpoint
- Custom exception handling
- Application and database health checks
- Swagger/OpenAPI documentation
- Environment-based configuration

### 🔨 In Development

- Role-based authorization
- Admin access control
- Shopping cart
- Orders and checkout
- Inventory management
- Payment abstraction
- Automated testing
- Frontend
- Dockerization
- CI/CD
- Production deployment

---

## 🏗️ Architecture

```text
Client
   ↓
FastAPI Routers
   ↓
Service Layer
   ↓
Repository Layer
   ↓
SQLAlchemy ORM
   ↓
PostgreSQL
