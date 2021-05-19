from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Udacity AWS Cloud Devops Nanodegree Capstone project - Python Flask Web App!'

app.run(host='0.0.0.0', port=5000)