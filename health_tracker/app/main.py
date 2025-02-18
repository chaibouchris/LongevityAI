import logging
from fastapi import FastAPI
from app.routes import (
    user_router,
    blood_test_router,
    physical_activity_router,
    sleep_activity_router,
    health_score_router,
    system_health_average_router
)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize FastAPI application
app = FastAPI()

# Include routers for different functionalities
logging.info("Including routers...")
app.include_router(user_router.router)
app.include_router(blood_test_router.router)
app.include_router(physical_activity_router.router)
app.include_router(sleep_activity_router.router)
app.include_router(health_score_router.router)
app.include_router(system_health_average_router.router)
logging.info("All routers have been included.")

@app.get("/")
def home():
    """
    Root endpoint to verify that the API is running.
    """
    logging.info("Root endpoint accessed.")
    return {"message": "Welcome to - Health Tracker!"}
