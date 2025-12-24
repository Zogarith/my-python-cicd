import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    # This connects to the 'db' service defined in docker-compose
    conn = psycopg2.connect(host='db', database='myapp', user='user', password='pass')
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"<h1>CI/CD with Database!</h1><p>Connected to: {db_version}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)