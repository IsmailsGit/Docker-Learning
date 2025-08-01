# app.py

from flask import Flask #We start by importing flask, we are basically creating a new flask application instance
import redis
app = Flask(__name__)


@app.route('/') #Then we're defining a route for the route url which is forward slash / kind of like when you go to google.com/ but the / isn't there most of the time because thats the route url
def hello_world():
   db = redis.connect(
    host="mydb"
    user="root"
    passwd="my-secret-pw2"
    db="redis"
   )
   
   
    return f'Hello, world! We are using Redis' #So when someone vists the url the hello world function is called


if name == 'main':
    app.run(host='0.0.0.0', port=5000)