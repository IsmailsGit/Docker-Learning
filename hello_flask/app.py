# app.py

from flask import Flask
import MySQLdb
#We import the mysql database library as it is essential for establishing a connection to a mysql database, this library enables us to execute sql commands within our python application
import time
app = Flask(__name__)

# This function attempts to connect to the MySQL database, retrying if it fails
def connect_with_retry(retries=5, delay=3):
    # Loop up to 'retries' number of times (default is 5)
    for i in range(retries):
        try:
            # Try to connect to the MySQL database
            db = MySQLdb.connect(
                host="mydb",           # Hostname of the MySQL service defined in docker-compose
                user="root",           # MySQL username
                passwd="my-secret-pw", # Password for the user
                db="mysql"             # Database name to connect to
            )
            return db  # If connection is successful, return the db object
        except Exception as e:
            # If connection fails, print the error with attempt number
            print(f"Attempt {i+1} failed: {e}")
            time.sleep(delay)  # Wait for a few seconds before retrying
    # If all retries fail, raise an exception to stop the app
    raise Exception("Could not connect to MySQL after multiple attempts.")

@app.route('/')
def hello_world():
    print("Attempting to connect to MySQL...")
    db = connect_with_retry()
    print("Connected to MySQL!")
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    print(f"MySQL version fetched: {version}")
    return f'Hello, World! MySQL version: {version[0]}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)