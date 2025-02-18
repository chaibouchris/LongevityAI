import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
DB_USERNAME = os.getenv("DB_USERNAME", "root")  # MySQL username
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")  # MySQL password
DB_HOST = os.getenv("DB_HOST", "localhost")  # MySQL host (default: localhost)
DB_NAME = os.getenv("DB_NAME", "health_tracker")  # Database name

# SQLAlchemy database URL
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
