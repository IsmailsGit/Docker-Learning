from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis( #Instantiate a Redis client, connecting to local host on port 6379
     host="redis",
     port=6379,
     db=0 #The default Redis database index
)

@app.route("/")
def home_page():
     return "Welcome to my Flask + Redis homepage!"

@app.route("/count")
def count_page():

     r.incr("visit_count")
     count = r.get("visit_count")
     return f"This is the visit count: {count.decode()}"

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)

#To make this work run redis first by doing docker run -d --name my-redis -p 6379:6379 redis:latest
#Then you can build the image docker build -t redis-flask .
#And finally to run the container you do docker run -p 5000:5000 redis-flask
#If you make a docker-compose.yml file there is no need to do any of this ^


