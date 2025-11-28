from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    return "Backend is working!"

@app.route("/db")
def dbcheck():
    try:
        connection =mysql.connector.connect(
    host="10.160.0.2",   # or localhost
    user="appuser",
    password="AppPass123!",
    database="appdb"
)
        cursor = db.cursor()
        cursor.execute("SELECT DATABASE();")
        print(cursor.fetchone())
        result = cursor.fetchone()
        return str(result[0])
    except Exception as e:
        return "Database connection failed: " + str(e)

app.run(host="0.0.0.0", port=5000)
