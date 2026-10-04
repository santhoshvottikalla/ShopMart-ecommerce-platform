
# ShopMart

> Production-oriented e-commerce backend built with Python, FastAPI,
> SQLAlchemy, and PostgreSQL.

ShopMart is a scalable e-commerce backend developed using a layered
architecture with clear separation between API handling, business logic,
data access, and database persistence.

The project focuses on clean architecture, secure authentication,
database integrity, maintainability, and production-oriented backend
engineering.

------------------------------------------------------------------------

## 🚧 Project Status

**Current Version:** `0.x` --- Backend Foundation + Authentication

### ✅ Implemented

-   FastAPI REST API
-   PostgreSQL integration
-   SQLAlchemy ORM
-   Layered architecture
-   Repository and Service layers
-   Pydantic validation
-   Dependency injection
-   Product CRUD APIs
-   Category CRUD APIs
-   User registration and login
-   bcrypt password hashing
-   JWT authentication
-   Bearer token authentication
-   Authenticated user endpoint
-   Custom exception handling
-   Application and database health checks
-   Swagger/OpenAPI documentation
-   Environment-based configuration

### 🔨 In Development

-   Role-based authorization
-   Admin access control
-   Shopping cart
-   Orders and checkout
-   Inventory management
-   Payment abstraction
-   Automated testing
-   Frontend
-   Dockerization
-   CI/CD
-   Production deployment

------------------------------------------------------------------------

## 🏗️ Architecture

``` text
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
```

  Layer        Responsibility
  ------------ ---------------------------------
  Router       HTTP requests and responses
  Schema       Request/response validation
  Service      Business logic
  Repository   Database access
  Model        Database representation
  Utils        Security and reusable utilities
  Exceptions   Application errors

------------------------------------------------------------------------

## 🔐 Authentication

ShopMart uses **JWT authentication** and **bcrypt password hashing**.

### Authentication Flow

``` text
Register
   ↓
Hash Password
   ↓
Store User
   ↓
Login
   ↓
Verify Credentials
   ↓
Generate JWT
   ↓
Bearer Token
```

### Endpoints

  Method   Endpoint                  Description
  -------- ------------------------- ------------------------
  `POST`   `/api/v1/auth/register`   Register user
  `POST`   `/api/v1/auth/login`      Login and receive JWT
  `GET`    `/api/v1/auth/me`         Get authenticated user

Protected endpoints use:

``` http
Authorization: Bearer <access_token>
```

------------------------------------------------------------------------

## 📦 Product API

  Method     Endpoint                  Description
  ---------- ------------------------- ----------------
  `GET`      `/api/v1/products`        List products
  `GET`      `/api/v1/products/{id}`   Get product
  `POST`     `/api/v1/products`        Create product
  `PUT`      `/api/v1/products/{id}`   Update product
  `DELETE`   `/api/v1/products/{id}`   Delete product

Validation includes product name, price, stock, category existence,
duplicate products, and product IDs.

------------------------------------------------------------------------

## 🗂️ Category API

  Method     Endpoint                    Description
  ---------- --------------------------- -----------------
  `GET`      `/api/v1/categories`        List categories
  `GET`      `/api/v1/categories/{id}`   Get category
  `POST`     `/api/v1/categories`        Create category
  `PUT`      `/api/v1/categories/{id}`   Update category
  `DELETE`   `/api/v1/categories/{id}`   Delete category

------------------------------------------------------------------------

## 🛒 Planned E-Commerce Workflow

``` text
User Registration
       ↓
Login
       ↓
Browse Products
       ↓
Add to Cart
       ↓
Checkout
       ↓
Validate Stock
       ↓
Create Order
       ↓
Payment
       ↓
Order Confirmation
```

Stock will be reduced during checkout rather than when products are
added to the cart.

Checkout will use database transactions and appropriate locking to help
prevent overselling.

------------------------------------------------------------------------

## 🗄️ Database

ShopMart uses PostgreSQL with the following core entities:

``` text
users
categories
products
carts
cart_items
orders
order_items
payments
```

### Relationships

``` text
User       1 ─── 1  Cart
User       1 ─── N  Orders
Category   1 ─── N  Products
Cart       1 ─── N  CartItems
Product    1 ─── N  CartItems
Order      1 ─── N  OrderItems
Product    1 ─── N  OrderItems
Order      1 ─── 1  Payment
```

------------------------------------------------------------------------

## 🧰 Technology Stack

### Backend

-   Python 3
-   FastAPI
-   SQLAlchemy
-   Pydantic
-   Uvicorn

### Database

-   PostgreSQL

### Security

-   bcrypt
-   JWT

### Development

-   Git
-   GitHub
-   Swagger / OpenAPI

### Planned

-   Pytest
-   Docker
-   GitHub Actions
-   Redis
-   Cloud deployment

------------------------------------------------------------------------

## 📁 Project Structure

``` text
shopmart/
└── backend/
    ├── app/
    │   ├── models/
    │   ├── schemas/
    │   ├── repositories/
    │   ├── services/
    │   ├── routers/
    │   ├── exceptions/
    │   ├── utils/
    │   ├── database.py
    │   └── main.py
    │
    ├── .env
    ├── .gitignore
    ├── requirements.txt
    └── venv/
```

> `.env` and `venv/` are excluded from Git.

------------------------------------------------------------------------

## ⚙️ Local Setup

### Prerequisites

-   Python 3.x
-   PostgreSQL
-   Git

### 1. Clone

``` bash
git clone https://github.com/santhoshvottikalla/shopmart.git
cd shopmart/backend
```

### 2. Create Virtual Environment

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure `.env`

``` env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/shopmart

JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> Never commit `.env` or production secrets to GitHub.

### 5. Run the Server

``` bash
uvicorn app.main:app --reload
```

API:

``` text
http://127.0.0.1:8000
```

------------------------------------------------------------------------

## 📚 API Documentation

### Swagger UI

``` text
http://127.0.0.1:8000/docs
```

### ReDoc

``` text
http://127.0.0.1:8000/redoc
```

------------------------------------------------------------------------

## ❤️ Health Checks

``` http
GET /health
GET /health/database
```

Example:

``` json
{
  "status": "healthy"
}
```

------------------------------------------------------------------------

## 🧠 Engineering Decisions

-   **Layered architecture** for separation of concerns.
-   **Repository pattern** to isolate database operations.
-   **Service layer** for business logic.
-   **OOP** through services, repositories, models, and business
    methods.
-   **JWT authentication** for stateless API authentication.
-   **bcrypt** for secure password hashing.
-   **Database constraints** for data integrity.
-   **Transactional checkout** for safer inventory management.

------------------------------------------------------------------------

## 🔒 Security

### Current

-   bcrypt password hashing
-   JWT authentication
-   Bearer tokens
-   Pydantic validation
-   Database constraints
-   Environment-based secrets
-   Protected authenticated endpoints
-   Centralized exception handling

### Planned

-   Role-based access control
-   Admin authorization
-   Rate limiting
-   Improved token management
-   Security testing
-   Production secret management
-   Audit logging

------------------------------------------------------------------------

## 🧪 Testing

Automated testing will be introduced during the production-readiness
phase.

Planned coverage:

-   Unit tests
-   Integration tests
-   API tests
-   Authentication tests
-   Database tests
-   Checkout transaction tests

A separate test database will be used instead of the development
database.

------------------------------------------------------------------------

## 🗺️ Roadmap

### Phase 1 --- Backend Foundation

-   [x] FastAPI setup
-   [x] PostgreSQL integration
-   [x] SQLAlchemy models
-   [x] Repository layer
-   [x] Service layer
-   [x] Product APIs
-   [x] Category APIs
-   [x] Exception handling
-   [x] Health checks
-   [x] Swagger/OpenAPI

### Phase 2 --- Authentication & Authorization

-   [x] Registration
-   [x] Password hashing
-   [x] Login
-   [x] JWT generation
-   [x] JWT validation
-   [x] `/auth/me`
-   [ ] Role-based authorization
-   [ ] Admin access control

### Phase 3 --- E-Commerce

-   [ ] Shopping cart
-   [ ] Orders
-   [ ] Checkout
-   [ ] Inventory management
-   [ ] Payments

### Phase 4 --- Production Readiness

-   [ ] Automated tests
-   [ ] Pagination
-   [ ] Search and filtering
-   [ ] Logging
-   [ ] Docker
-   [ ] CI/CD
-   [ ] Cloud deployment
-   [ ] Frontend

------------------------------------------------------------------------

## 🚫 V1.0 Out of Scope

The initial version will not include:

-   Microservices
-   Kubernetes
-   Kafka
-   Elasticsearch
-   Recommendation engines
-   Real financial payment processing
-   Multi-region deployment
-   Complex warehouse management
-   Real-time delivery tracking

These may be considered in future versions when justified by actual
requirements.

------------------------------------------------------------------------

## 🎯 Project Goals

ShopMart is designed to demonstrate practical experience with:

-   Python
-   Object-Oriented Programming
-   FastAPI
-   REST APIs
-   PostgreSQL
-   SQLAlchemy
-   Relational database design
-   Authentication and authorization
-   Software architecture
-   Business logic
-   Database transactions
-   Error handling
-   Git and GitHub
-   Automated testing
-   Docker
-   Deployment

The goal is to evolve ShopMart from a basic shopping application into a
maintainable, secure, and production-oriented backend.

------------------------------------------------------------------------

## 👨‍💻 Author

**Santhosh Vottikalla**

B.Tech Computer Science & Engineering\
Indian Institute of Technology Tirupati

GitHub:\
https://github.com/santhoshvottikalla

Repository:\
https://github.com/santhoshvottikalla/shopmart

------------------------------------------------------------------------

## 📄 License

This project is currently developed as a portfolio and learning project.

License information will be added before the first stable release.

------------------------------------------------------------------------

**ShopMart is actively under development.**
