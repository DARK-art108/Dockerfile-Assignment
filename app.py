import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/What is Your Name')
def hello():
    return 'My Name is Ritesh'

if __name__ == "__main__":
    app.run()
