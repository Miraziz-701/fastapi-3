import os
from dotenv import load_dotenv


load_dotenv(".env")

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
# DB_PORT = os.getenv('DB_PORT')
SECRET_KEY = os.getenv('S_KEY')
ALGORITHM = os.getenv('ALGO')

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"