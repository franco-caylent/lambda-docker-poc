from flask import Flask
import os, json

from flask.json import jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "this is the default endpoint"

@app.route("/version")
def version():
    return os.environ["VERSION"]

@app.route("/hello/<name>")
def hello(name):
    return "hello {}!".format(name)

def handler(event, context):
    return {
            "statusCode": 200,
            "statusDescription": "200 OK",
            "isBase64Encoded": False,
            "headers": {
                "Content-Type": "text/html; charset=utf-8"
            },
            "body": "this is the default endpoint"
        }

def hello_handler(event, context):
    #print(hello(event['path'].split("/")[2]))
    return {
            "statusCode": 200,
            "statusDescription": "200 OK",
            "isBase64Encoded": False,
            "headers": {
                "Content-Type": "text/html; charset=utf-8"
            },
            "body": hello(event['path'].split("/")[2])
        }
        

def version_handler(event, context):
    return {
            "statusCode": 200,
            "statusDescription": "200 OK",
            "isBase64Encoded": False,
            "headers": {
                "Content-Type": "text/html; charset=utf-8"
            },
            "body": str(version())
        }