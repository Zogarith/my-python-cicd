import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    # Use 'DATABASE_URL' if it exists (for Render and GitHub)
    # Fall back to 'db' host if it doesn't (for local Docker)
    db_url = os.getenv('postgresql://my_cicd_db_user:dup6U837TMSvMAosp1Vd1tCLOtEoc8rx@dpg-d55o1iumcj7s73ff6320-a/my_cicd_db', 'postgres://user:pass@db:5432/myapp')
    conn = psycopg2.connect(db_url)
    return conn

@app.route('/')
def home():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"<h1>CI/CD with Database!</h1><p>Connected to: {db_version[0]}</p>"
    except Exception as e:
        # This will help you see the EXACT error on the website
        return f"<h1>Connection Error</h1><p>{str(e)}</p>", 500