from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

env = {
    "POSTGRES_USER": os.getenv("POSTGRES_USER"),
    "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    "POSTGRES_HOST": os.getenv("POSTGRES_HOST"),
    "POSTGRES_PORT": os.getenv("POSTGRES_PORT"),
    "POSTGRES_DB": os.getenv("POSTGRES_DB"),
    "APP_SETTINGS": os.getenv("APP_SETTINGS"),
}

db_url = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (
    env["POSTGRES_USER"],
    env["POSTGRES_PASSWORD"],
    env["POSTGRES_HOST"],
    env["POSTGRES_PORT"],
    env["POSTGRES_DB"],
)


def check_env() -> None:
    for key, value in env.items():
        if not value:
            raise ValueError(f"Ensure {key} is set in '.env' file")
