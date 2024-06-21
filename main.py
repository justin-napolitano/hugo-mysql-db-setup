from MySQLConnector import MySQLConnector

from dotenv import load_dotenv
import os



if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    connection = MySQLConnector()
    connection.connect()
    connection.disconnect()