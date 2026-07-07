import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load .env from the config folder
load_dotenv(Path(__file__).parent / ".env")

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)