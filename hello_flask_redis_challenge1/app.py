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
#SET command: store a string value under 'foo'
  #   r.set("visit_count")
     r.incr("visit_count")
#GET command: retrieve the value stored at 'foo'
   #  r.get("visit_count")
   #  return f"This is the value: {value.decode()}"
     count = r.get("visit_count")
     return f"This is the visit count: {visiters.decode()}"
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)







#from flask import Flask  

#app = Flask(__name__) 

#@app.route("/") 
#def hello(): 
#     return "Hello, Flask!" 
#@app.route("/greet") 
#def greet(): 
 #    return "Hello from the /greet route!" 
#if __name__ == "__main__": 
 #    app.run(host="0.0.0.0", port=5000)