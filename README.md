# ShopMart

> A production-oriented e-commerce backend built with Python, FastAPI, SQLAlchemy, and PostgreSQL.

ShopMart is an e-commerce platform currently being developed with a layered backend architecture designed for maintainability, scalability, and future deployment.

The project is being developed incrementally from a prototype into a complete web-based shopping platform.

---

## 🚧 Project Status

**Current Version:** `0.x` — Backend Foundation

The current implementation includes:

- FastAPI backend
- PostgreSQL database integration
- SQLAlchemy ORM
- Product management APIs
- Category management APIs
- Repository layer
- Service layer
- Pydantic request/response schemas
- Custom application exceptions
- Dependency injection
- API health checks
- Swagger/OpenAPI documentation

Authentication, cart, checkout, orders, payments, testing, frontend, containerization, and deployment are planned for upcoming versions.

---

## 🎯 Project Goals

The goal of ShopMart is to build a complete e-commerce platform while following professional software engineering practices.

The project focuses on:

- Clean architecture
- Separation of responsibilities
- Object-oriented design
- RESTful API development
- Database-backed applications
- Input validation
- Business logic isolation
- Secure authentication
- Transaction-safe order processing
- Automated testing
- Containerization
- CI/CD
- Deployment

---

## 🏗️ Architecture

ShopMart follows a layered backend architecture:

```text
Client
   │
   ▼
FastAPI Routers
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL