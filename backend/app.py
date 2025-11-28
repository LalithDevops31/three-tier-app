from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    return "Backend is working!"

@app.route("/db")
def dbcheck():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="devuser",
            password="devpass",
            database="devdb"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 'Database Connected Successfully!'")
        result = cursor.fetchone()
        return str(result[0])
    except Exception as e:
        return "Database connection failed: " + str(e)

app.run(host="0.0.0.0", port=5000)
