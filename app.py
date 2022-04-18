# import dependency
from flask import Flask
# create new flask app instance
app = Flask(__name__)
# create flask route
@app.route("/")
def hello_world():
    return 'Hello world'
# run flask app -- had to run in command line according to CS YouTube video
# export FLASK_APP=app.py
# flask run