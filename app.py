from flask import Flask,send_file

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello, this is a Flask web server!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)