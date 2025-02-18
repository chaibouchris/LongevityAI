import logging
from sqlalchemy import text
from app.db.database import engine, Base
from app.db.models import User, PhysicalActivity, SleepActivity, BloodTest, HealthScore, SystemHealthAverage

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Checking database connection...")
logging.info(f"Connecting to: {engine.url}")

# Drop all tables to ensure schema updates
logging.warning("Dropping all tables (to ensure schema updates)...")
Base.metadata.drop_all(bind=engine)

# Create all tables
logging.info("Creating tables...")
Base.metadata.create_all(bind=engine)

logging.info("Verifying if tables exist in the database...")

# Query to check existing tables
with engine.connect() as connection:
    try:
        result = connection.execute(text("SHOW TABLES;"))  # Adjusted for MySQL
        tables = [row[0] for row in result.fetchall()]
        if tables:
            logging.info(f"Existing tables: {tables}")
        else:
            logging.warning("No tables found! Something is wrong.")
    except Exception as e:
        logging.error(f"Error while fetching tables: {e}")

logging.info("Database initialization completed.")
