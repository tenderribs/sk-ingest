from env import env


class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{env['POSTGRES_USER']}:{env['POSTGRES_PASSWORD']}@{env['POSTGRES_HOST']}:{env['POSTGRES_PORT']}/{env['POSTGRES_DB']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
