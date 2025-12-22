# import the Flask class from flask module
from flask import Flask, jsonify

# create an instance of the flask class, by passing in name of module
app = Flask(__name__)

# define a route for the root URL ('/')
@app.route('/')

# create function that handles the url request
def hello_world():
    return {"message": "Hello World"}