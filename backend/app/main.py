from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db
from app.routers.products import router as product_router
from app.routers.categories import router as category_router


app = FastAPI(
    title="ShopMart API",
    description="Production-oriented e-commerce platform",
    version="1.0.0"
)


# Include API routers
app.include_router(product_router)
app.include_router(category_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to ShopMart API",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/health/database")
def database_health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected"
    }