from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")  # Root route
def home():
    return "Flask API is Running Successfully!"

@app.route("/api/data", methods=['GET'])  # JSON response
def get_data():
    return jsonify({"message": "This is JSON data from Flask!"})

if __name__ == "__main__":
    app.run(debug=True)



import psycopg2

DB_NAME = "HostelHive"
DB_USER = "myuser"
DB_PASSWORD = "mypassword"
DB_HOST = "my-postgres"
DB_PORT = "5432"

def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
