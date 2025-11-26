from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

load_dotenv(BASE_DIR / "path.env")

load_dotenv(BASE_DIR / "api_key.env")

DATABASE = BASE_DIR / "database"
API_KEY = os.getenv("API_KEY")