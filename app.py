"""
This module contains a simple Flask app that returns 'Hello World!'
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Route to return 'Hello World!'"""
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
