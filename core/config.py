# coding=utf-8
from dotenv import load_dotenv

load_dotenv()


class DbSetting:

    DB_USERNAME = "thadmin"
    DB_PASSWORD = "thadmin123"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_DATABASE = "thdb"

    DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"


settings = DbSetting()
