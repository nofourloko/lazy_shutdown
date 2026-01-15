from flask import Flask
import os 
import socket

app = Flask(__name__)

# Define a single endpoint
@app.route('/')
def home():
    os.system("shutdown /s /t 0")
    return "Shutting down computer"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
