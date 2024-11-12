# coding=utf-8
from dotenv import load_dotenv
import os
import configparser
import ctypes

load_dotenv()


class DbSetting:

    main_conf = configparser.ConfigParser()
    main_conf.read("MainConfig.ini")

    information = main_conf["information"]

    database_id = information["database_id"]
    database_password = information["database_password"]
    database_ip = information["database_ip"]
    database_port = information["database_port"]
    database_name = information["database_name"]

    DATABASE_URL = f"postgresql://{database_id}:{database_password}@{database_ip}:{database_port}/{database_name}"


settings = DbSetting()
