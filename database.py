
import mysql.connector
from dotenv import load_dotenv
from exceptions import DatabaseConnectionError
import os

load_dotenv()

class Database:

    def __init__(self)->None:
        self.create_database('kalivachat')
        self.create_tables()
    

    def create_database(self, db_name: str) -> None:
        with self.connect_server() as conn:
            cur = conn.cursor()
            cur.execute(f"""
            CREATE DATABASE IF NOT EXISTS {db_name}""")
            conn.commit()

    def create_tables(self) ->None:
        with self.connect_database() as conn:
            cur = conn.cursor()
            self.create_users_table(cur)
            self.create_messages_table(cur)
            conn.commit()

    def connect_database(self) ->mysql.connector:
        try:
            return mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('USER'),
                database=os.getenv('database'),
                password=os.getenv('PASSWORD')
            )
        except Exception as e:
            raise DatabaseConnectionError(f"database connection Error: {str(e)}")

    def connect_server(self) ->mysql.connector:
        try:
            return mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('USER'),
                password=os.getenv('PASSWORD')
            )
        except Exception as e:
                    raise DatabaseConnectionError(f"database connection Error: {str(e)}")

    def create_users_table(self, cur) ->None:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(128) UNIQUE,
            password_hash VARCHAR(512)
        )""")

    def create_messages_table(self, cur) ->None:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT NOT NULL,
            message VARCHAR(1024),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )""")


