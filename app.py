from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>SAnthOsh</h1><p>HOW ARE YOU .</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
