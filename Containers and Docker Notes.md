 # Introduction to Containers and Docker 
## What are Containers?
Containers are lightweight, portable units for running applications.
<br> They bundle an application with all its dependencies ensuring it runs consistently across different environments.
<br> For example, if you have an application and you want to run every part of the application, containers will include the code, the runtime, the libraries and anything you need including all dependencies that the application needs in order to run 
and because they're isolated it runs the same on any environment you want to run it on. 

Think of containers like shipping containers just like how shipping containers hold everything needed for goods to be transported and can be easily moved from ships and trains, Software containers hold everything needed for an application to run and can be easily moved from one environment to another.

![Screenshot](https://github.com/user-attachments/assets/68273fd3-18a2-48e3-a247-1aa3a8ccdd89)

The infrastructure(your laptop or host machine) represents the physical or virtual hardware where everything runs.
<br> The host operating system is the operating system that runs directly on the infrastructure e.g. MacOS or Windows.
<br> The docker engine is what makes containerization possible, it provides the environment to build, run and manage containers. Without the docker engine your containers would be useless and won't run.
<br> On top of the docker engine there is the docker containers, each container holds an application and all its dependencies so the binaries and libraries that the application requires to run. This isolation ensures that each app runs consistently regardless of the environment and each container doesn't interfere with each other. 

### Benefits of Containers
Isolation - Isolation helps prevent conflict and ensures that applications run smoothly without interfering with each other.
<br> Consistency - Containers provide a consistent environment for applications to run, this means that the application behaves the same way regardless of where it's deployed, eliminates anyone from having any problems like this machine only works on windows and not mac os, due to missing dependencies or different configurations.
<br> Efficiency - Containers are more resource efficient compared to traditional virtual machines, they share the host kernel(host operating system), the docker engine sits above the host os which means the containers share the host system's kernal(operating system). This allows for more containers to run on the same hardware and makes containers faster to start up compared to virtual machines.

## What is Docker?
Docker is an open platform for developing, shipping and running applications in containers.
<br> It simplifies the process of managing containers, making it easier to build, deploy and run applications.
<br> Docker has several key components that make it such a powerful tool:
Docker Engine - Docker Engine is the core component of Docker that enables building, running, and managing containers. It uses Dockerfiles to build container images, and those images are then used to create and run containers. Think of it like the engine of a car—it powers the entire container lifecycle.
<br> Docker Hub - A cloud service for sharing applications and automating workflows. It is basically a repository where you can find and share container images, its like the app store for docker images, you can pull official images, community contributed images or even share your own images with others.
<br>
Docker Compose - It is essentially a tool for defining and running multi container docker applications(Will go in detail later on).
Images - Images are templates for creating containers, you can think of an image as a snapshot of an application at a certain point in time.
<br> Images are immutable, which means that they don't change once they're created and the only way to change them is by recreating the image.
<br> The immutability ensures that the application runs consistently no matter where it's deployed.
<br> Containers on the other hand are the running instances of images, for example if an image is a recipe a container is the dish you create from it. Containers are what you actually interact with, they run your application and you can start, stop and modify them as needed. 
<br> Docker file - A docker file is a file used to build docker images, it contains a series of instructions that docker uses to assemble an image 

Docker workflow
<br> You create a docker file which is your recipe
<br> You create an image which is your snapshot of the application at a given point in time
Then you run it as a container
### Importance in Modern Development 
1. Simplified Deployment - One of the biggest challenges in software development is ensuring that applications work consistently across different environments. Docker solves this problem by creating a consistent environment from development all the way to production.
2. Improved Efficiency - Traditional virtual machines can be resource heavy and slow to start, in contrast docker containers are lightweight and share the host systems kernel which allows them to start up almost instantly and use fewer resources. This efficiency is crucial in modern development where developers can spin up containers in seconds which make easier to test and deploy applications rapidly.
3. Enhanced Collaboration - Docker makes it easy to share development environments and applications with team members, instead of setting up complex environments on each developers machine you can create a docker image and share it with your team.
4. Streamlines workflows by integrating seamlessly with CI CD pipelines, this allows for automated testing, building and deployment of containers.

![Screenshot](https://github.com/user-attachments/assets/fd0f3a03-24db-4640-bee7-14a4790697bf)
<br>A virtual machine allows multiple operating systems to run on a single physical machine.
The infrastructure(your laptop or host machine) represents the physical or virtual hardware where everything runs.
<br> The host operating system is the operating system that runs directly on the infrastructure e.g. MacOS or Windows.
<br> The hypervisor is responsible for creating and managing virtual machines by allocating resources like cpu, memory and storage. Each vm runs a full guest operating system which is completely isolated from others.
<br> Within each vm you have the guest operating system which is another different operating system running on top of the host. Each vm has its own binaries, libraries and anything an application would need to run.

### VMs(Virtual Machines) vs Containers
<br>Key differences between the two 
<br>
Each vm needs to boot up a full guest ❌ |Startup Time| ✅ Containers share the host     system which operating can take minutes            |            operating system so they can start                                                                              within seconds.  
<br>Each vm includes a full operating  ❌|Resource Usage|✅ Containers are more efficient 
operating which consumes significant resources.    |       using only what's necessary for the                                                              application and its dependencies
<br>Vm's provide a strong isolation   ✅ |Isolation| ❌  Containers offer process level 
with each vm  having its own operating system    |   isolation, they share the host os                                                                kernel but they're isolated within the                                                           container itself, the process is                                                                  running within the container
<br> Vm's are less portable due to their❌|Portability|✅Containers are highly portable and can 
size and dependency on specific hypervisors      |    run consistently across different                                                               environments thanks to dockers image format
## Introduction to Docker File and Docker Images
docker --version - Shows you the version of docker
<br> docker info - Gives a comprehensive overview of your docker environment, useful if you want to troublshoot or understand the system's current state. 
<br> docker ps - Shows you all the running containers, when it was created, the status etc.
<br> docker ps -a - This lists all containers including the stopped ones. 
<br> docker build -t imagename . - This builds a docker image the docker build part of the command initiates the build process, the -t tags the image with a name in this case imagename, the . represents the current directory and tells docker to look for the docker file there, if we were in a different directory we would do ./ and then the name of the directory your docker file is in.
<br> docker run -d -p 5002:5002 nameofthecontainerwe'reusing - the -d runs the container in detached mode which means running it in the background and the -p followed by the ports is mapping the port 5002 on my machine to the port 5002 in the container and then the name of the image we're using

Understanding Dockerfile
A docker file is just a series of instructions on how to build the docker image.
<br> Each instruction in a docker file creates a layer in the image, which makes it easier to track changes and optimize your builds. 

5 Key Commands
<br> FROM - Specifies the base image to use for the docker image, the base image serves as the foundation for your application.
<br> RUN - Executes commands in the container, this instruction is used to install packages and update dependencies.
<br> COPY - Copies files from the host machine into the container, this is how you bring your applications code and configuration into the container. 
<br> WORKDIR - Sets the working directory for subsequent instructions, this ensures that the command runs in the correct directory within the container 
<br> CMD - Specifies the command to run when the container starts, when the container starts it'll run this command

<br> Example Dockerfile
<br> #The from instruction sets the base image for your docker image in this case we're using the official Node.js image.
<br> FROM node:14
<br> #The workdir instruction sets the working directory inside the container, this is where instructions like copy and run will be executed
<br> WORKDIR /app
<br> #This is copying files from your host machine to the container, we're copying the package.json and the package-lock.json files to install dependencies  
<br> COPY package*.json ./
<br> The run instruction executes commands in the container, we're using it to run npm install to install the node js dependencies
<br> RUN npm install
<br> #Copies the rest of the application code 
<br> COPY ..
<br> #The expose instruction tells docker that the container will listen on the specified network ports at runtime which in this case is 3000, this is useful for when you want to run the container and expose ports to the host machine 
<br> #This specifies the command to run when the container starts, here we are starting a node js application by running node index.js 
<br> CMD ["node", "index.js"]

### Create a Simple Web Application to Dockerise.
Python will be used in this but you don't need to really know what it does, also be using flask flask is a simple and lightweight framework for creating web applications in python.
<br> Make a directory mkdir hello_flask
<br> Make a python file touch app.py
<br> from flask import Flask #We start by importing flask, we are basically creating a new flask application instance 
<br> app = Flask(__name__)

<br> @app.route('/') #Then we're defining a route for the route url which is forward slash / kind of like when you go to google.com/ but the / isn't there most of the time because thats the route url
<br> def hello_world():
<br>     return 'Hello, world!' #So when someone vists the url the hello world function is called

<br> if  __name__ == '__main__':
<br>     app.run(host='0.0.0.0', port=5000) #We are running the application by doing app.run we're using the variable name flask and telling it to run on our local host which is 0.0.0.0 and we're doing this on port 5000 
<br> To run this application on the command line without docker you do python3 app.py
### Containerise our Web Application with Docker
<br> Now we will take that web application that we made and containerise it using docker
<br> First we need to write a docker file, the docker file is a text file that containes a series of instructions on how to build a container image for our application
We do touch Dockerfile, You have to capitalise the first letter when creating a dockerfile and it doesn't have an extension.

#We use the python image and the version
<br> FROM python:3.8-slim
<br> #We are setting the work directory so that any commands after this will be run in this directory
<br> WORKDIR /app
<br> #We are going to copy all of the files from our current directory
<br> COPY . .
<br> #We install flask
<br> RUN pip install flask
<br> #We expose port 5002, we are making this port available so we can access the container from our local host, this makes the application accessible from outside the container 
<br> EXPOSE 5002
<br> #The cmd command tell docker to run our python application
<br> CMD ["python", "app.py"]

Next step is to build your docker image use the command below

docker build -t imagename . - This builds a docker image the docker build part of the command initiates the build process, the -t tags the image with a name in this case imagename, the . represents the current directory and tells docker to look for the docker file there, if we were in a different directory we would do ./ and then the name of the directory your docker file is in.
<br> After it builds a docker image we wull run it as a container to do that use the command below
<br> docker run -d -p 5002:5002 nameofthecontainerwe'reusing - the -d runs the container in detached mode which means running it in the background and the -p followed by the ports is mapping the port 5002 on my machine to the port 5002 in the container and then the name of the image we're using


## Introduction to Docker Networking
### Basic Networking Concepts in Docker
Understanding basic networking concepts in docker is essential for managing containerised applications effectively 
<br> Docker provides several default network options that you can use to manage how containers commmunicate

Bridge Network - A bridge network is a default network mode for containers on the same machine. Containers connected to the bridge network can communicate with each other using their own ip addresses. It's isolated from your host machines network which provides an extra layer of seccurity

Host Network - In host mode, a container uses the host machines network directly without any isolation, this mode is useful for applications that need to closely interact with the host system.

None type - This option gives a container no network interface at all which makes it completely isolated, it's used when you want to ensure that a container has no network access whatsoever which could be useful for certain security scenarios.

In the context of DevOps, docker networking is particularly important because it simplifies the implementation of microservices architecture, microservices allow different parts of an application to run as independent services each in its own container. Docker networking ensures that these services can communicate with each other efficiently and securely.

### Linking Containers together
Before this I already created the flask(flask is a simple and lightweight framework for creating web applications in python) app.py that says hello world and containerised it with docker

By connecting our flask app to a mysql database we're simulating a real world scenario where web applications often rely on databases to store and retrieve data.

app.py
<br> from flask import Flask
<br> import MySQLdb
<br> #We import the mysql database library as it is essential for establishing a connection to <br> a mysql database, this library enables us to execute sql commands within our python application
<br> app = Flask(__name__)

@app.route('/')
<br> def hello_world():
<br>   #Connect to the MySQL database
<br>    db = MySQLdb.connect( #We are trying to establish a connection with the mysql database
<br>        host="mydb",    # Hostname of the MySQL container
<br>        user="root",    # Username to connect to MySQL
<br>        passwd="my-secret-pw",  # Password for the MySQL user
<br>        db="mysql"      # Name of the database to connect to
<br>   )
<br>   cur = db.cursor()
<br>   cur.execute("SELECT VERSION()")
<br>   version = cur.fetchone()
<br>   return f'Hello, World! MySQL version: {version[0]}'

if __name__ == '__main__':
<br>   app.run(host='0.0.0.0', port=5002)

Dockerfile
#We use the python image and the version
<br> FROM python:3.8-slim
<br> #We are setting the work directory so that any commands after this will be run in this directory
<br> WORKDIR /app
<br> #We are going to copy all of the files from our current directory
<br> COPY . .
<br> RUN apt-get update && apt-get install -y \
         gcc \
         python3-dev \
         libmariadb-dev \
         pkg-config
 <br> #We install flask and the mysql client package, the pakcage is critical because it provides the tools needed to connect to a mysql data base from within our python app
<br> RUN pip install flask mysqlclient
<br> #We expose port 5002, we are making this port available so we can access the container from our local host, this makes the application accessible from outside the container 
<br> EXPOSE 5002
<br> #The cmd command tell docker to run our python application
<br> CMD ["python", "app.py"]

Before we move on to the process of building and running our updated containers we need to create a custom network> Why a custom network? In docker creating a custom network allows containers to communicate with each other using container names instead of ip addresses, this is useful as we need the flask app to interact with the mysql database.

We are going to use the command docker network create my-custom-network, this command creates a network for us called the my-custom-network which we'll use to connect our flask and mysql containers together.

Next is running the containers first we'll run the mysql container to do this we'll do 
docker run -d --name mydb --network my-custom-network -e MYSQL_ROOT_PASSWORD=make-a-password mysql:5.7   - mydb is the container name im giving it  and i'm setting the network to my-custom-network so that we can connect our database container/mysql container to my custom network and here -e MYSQL_ROOT_PASSWORD=my-secret-pw we are setting the root password for the mysql database, this password is necessary for authentication when connecting to the database. Lastly we are going to specify the version of mysql by doing mysql:5.7

Now we're going to build the docker image for the flask app with the updated dockerfile
<br> docker build -t hello-flask-mysql .

Now we're going to run our flask application 
docker run -d --name myapp --network my-custom-network -p 5002:5002 hello-flask-mysql - -d is detached mode so its running in the background, --name myapp is the name i chose for it , we're also going to attach this container to the same network we attached our database container, we're going to use the ports 5002 on our local laptops to the port 5002 on our container, we're going to use the image hello-flask-mysql which is the image we just created.

Any debugging you need to do use the docker logs and then the container that isn't working for you e.g. docker logs myapp

### Introduction to Docker Compose
Docker Compose is a tool that allows you to define and manage multi container docker applications.
<br> Instead of manually starting and stopping containers one by one, docker compose lets you define all your services in a single file and manage them collectively.
<br> Imagine your application has several components, a web server, a database and a caching service. Docker compose acts as the organiser for these parts ensuring they work together smoothly.

At the heart of docker compose is a docker-compose.yaml file, this yaml file lists all the services your application needs, it's like a blueprint that describes each container specifying details like which image to use, which port to expose and how the containers should interact.
<br> Docker compose allows you to handle your entire stack with minimal effort

Also when you use docker compose, it automatically creates a network for your containers, now we don't have to actually create a custom network.
### Why is Docker Compose Important in DevOps?
Docker compose is an essential component of a streamlined efficient devops workflow

1. Makes Development and Testing Easier - One of the biggest challenges in development is setting up a consistent environment for coding and testing, docker compose simplifies this by allowing you to quickly spin up the exact environment you need with all of the necessary services, whether it's a web server, database, cache etc. Instead of manually setting up each service you define everything in a docker-compose.yaml file and run a single command to start the entire environment. This speed and simplicity means the developers can focus more on writing code and less on managing infrastructure.

2. Ensures Consistency -  A common issue in software development is code working on one developers machine but not on anothers. By defining the environment in a docker compose yaml file you guarantee that every developer, tester and cicd pipeline uses the exact same setup, it's consistency reduces bugs and errors leading to more reliable software.

3. Enhances Teamwork -  Collaboration is a cornerstone of devops and docker compose enhances teamwork, when every team member is using the same environment it becomes easier to share code, configurations and even the environment set up itself. Docker compose makes it simple to version control your infrastructure alongside your application code, e.g. when someone pulls the latest code from your repo they also get the exact environment set up needed to run the application. 

### Our First docker-compose.yml
Think of the docker-compose.yml file as a recipe that lists all the ingredients i.e. the services that your application needs, instead on launching each container separately you write down everything in this one file and docker compose takes care of the rest.

You can specify which docker image to use, how the containers should interact and even what ports to expose.

For our app.py hello world application that connects to a mysql database we are going to create a docker-compose.yml file that runs both services with just one command.

First we make the file so touch docker-compose.yml
<br> then copy and paste 
version: '3.8' #The version tells docker compose which version of the file format we're using 

<br> services: #The services is where we list all the different parts of our app, which is the web service(our flask application) and a database
<br>   web:
<br>   build: . #This tells docker compose to build the web service from the docker file in the current directory that's what the dot means
<br>    ports:
<br>     - "5002:5002" #We set the ports to 5002 for the web service
<br>   depends_on:
<br>     - db  #This line means that the web service depends on the database service, so docker compose will start the database service first before starting the web service

<br> db:
<br>   image: mysql:8 #We are using an image we found online, this tells docker compose which image version we're using
<br>   environment:
<br>   MYSQL_ROOT_PASSWORD: my-secret-pw  #We set the environment variable mysql root password which we set to my secret pw

Now with everything set up in the docker-compose.yml file we can start up both the flask application and the mysql database with just one command.
<br> docker-compose up - It tells docker compose to read the docker-compose.yml, build an necessary images and start all the services you've defined 
<br> docker-compose up -d - does the same thing but runs it in the background

Also changed app.py as it wasn't connecting to the mysql database properly and wasn't printing out the version here is the updated version

<br> from flask import Flask
<br>import MySQLdb
#We import the mysql database library as it is essential for establishing a connection to a mysql database, this library enables us to execute sql commands within our python application
<br>import time
<br>app = Flask(__name__)

#This function attempts to connect to the MySQL database, retrying if it fails
<br>def connect_with_retry(retries=5, delay=3):
    # Loop up to 'retries' number of times (default is 5)
<br>    for i in range(retries):
<br>      try:
<br>            # Try to connect to the MySQL database
<br>            db = MySQLdb.connect(
<br>            host="mydb",           # Hostname of the MySQL service defined in docker-compose
<br>            user="root",           # MySQL username
<br>            passwd="my-secret-pw", # Password for the user
<br>            db="mysql"             # Database name to connect to
<br>          )
<br>          return db  # If connection is successful, return the db object
<br>    except Exception as e:
<br>        # If connection fails, print the error with attempt number
<br>        print(f"Attempt {i+1} failed: {e}")
<br>        time.sleep(delay)  # Wait for a few seconds before retrying
<br>  # If all retries fail, raise an exception to stop the app
<br>  raise Exception("Could not connect to MySQL after multiple attempts.")

<br> @app.route('/')
<br> def hello_world():
<br>   print("Attempting to connect to MySQL...")
<br>   db = connect_with_retry()
<br>   print("Connected to MySQL!")
<br>   cur = db.cursor()
<br>   cur.execute("SELECT VERSION()")
<br>   version = cur.fetchone()
<br>   print(f"MySQL version fetched: {version}")
<br>   return f'Hello, World! MySQL version: {version[0]}'

if __name__ == '__main__':
<br> app.run(host='0.0.0.0', port=5002)
## Docker Registries
Where do docker images go after you've built them?
That's where docker registries come into play, docker registries are crucial for managing, storing and deploying your docker images.  

### Introduction to Docker Registries
Docker registry is a system for storing and sharing docker images.
<br> Think of a docker registry as a storage and distribution hub for your docker images, its where your images live when they're not running as containers.

Key Features
<br> Public Registries - A public registry like dockerhub is open to everyone, you can share your images with the world or use community provided images as the foundation for your applications.
<br> Private Registries - You have private registries like AWS ECR which is secure and restricted, so only you have access to these images and they allow you to control who has access to your images so you can make it public or private.

### Importance of Docker Registries in DevOps

1. Streamlines the deployment process - Once your docker images are stored in a registry, they can be easily accessed and deployed across multiple environments from development all the way to production, this makes it faster and more reliable to roll out new features or updates.

2. Enhances Collaboration within your team - When your images are stored in a centralised registry, everyone on your team has access to the same resources this makes it easier to share and manage images, improving teamwork and efficiency.

3. Ensures Consistency across different environments - By storing your images in a registry, you can be sure that the exact same image is being used in development, testing and production, eliminates the 'it only works on my machine' problem, ensuring what you've tested locally is exactly what runs in production.

How do Registries fit into the overall DevOps workflow?

Docker registries are used to build, so where you start building your docker image locally e.g. where we created a dockerfile and we built the image. 
<br> Before pushing the image to a registry you test it to ensure everything worked as expected, so you create a container out of it to make sure the application runs.
<br> Once the image is ready and the application runs as expected then you push the image to a docker registry like AWS ECR.
<br>Finally you pull that image from the registry to deploy it in your production or staging environment.

Future reference - This is where pipelines(CICD module) come in later on, where you are pulling the images that you've built directly from this registry, so once you've pushed the image to the registry, you're now pulling the image within your pipeline so you can do this automatically.
### DockerHub: A Popular Docker Registry
Dockerhub is basically a public registry where you can store, share and access docker images, it's like the app store for docker images.

Whether you want to use prebuilt images, share your own or collaborate with others DockerHub is the place to do it.

#### Pushing an image to DockerHub
<br> First we need to build and tag our image correctly to do this do the command underneath

docker build -t ismailsdocker1/flask-mysql:v1 . - -t means we're tagging it then my dockerhub username and forward slash the repository i made and then colon the tag, the tag can be something like latest or a version in this case i call it v1 for version 1. The dot tells docker to use the current directory as the build context where it will look for the docker file.

Then once our image is built and tagged we can push it to dockerhub, the command is 
docker push ismailsdocker1/flask-mysql:v1 - The command uploads your image to dockerhub under the specified repository name  

#### Pulling an image from DockerHub
docker pull ismailsdocker1/flask-mysql:v1 - docker pull followed by your dockerhub username, your repository name and the tag v1. You are downloading the image to your local machine where you can run it as a container.

#### Pushing our Images to Amazon ECR(Elastic Container Registry)
AWS ECR is a fully managed docker registry service thats great for storing and managing private docker images.

To log in to ecr from the command line do this command aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 043309335662.dkr.ecr.us-east-1.amazonaws.com - I got this from the ecr push commands page.

Build
We first build our docker image, we use this command docker build -t ecr-flask-mysql . - I got this from the aws push commands page

Tag
Just like we did with dockerhub, we need to tag our docker images before pushing it to ecr but the difference is that we also need to tag the image with the ecr repository url.
docker tag ecr-flask-mysql:latest 043309335662.dkr.ecr.us-east-1.amazonaws.com/ecr-flask-mysql:latest - You can get this from the aws push commands page.

Push
Next I have to push the docker image using the command docker push 043309335662.dkr.ecr.us-east-1.amazonaws.com/ecr-flask-mysql:latest - again you can get this from the aws push commands page

Pull
If you want to then pull this image to your local machine you do the command
docker pull 043309335662.dkr.ecr.us-east-1.amazonaws.com/ecr-flask-mysql:latest - Same command as the docker push but you just change it pull. It's pulling the image that's stored in our ecr repository to our local docker environment ready to by run as a container.

Run as a container 
#Create a custom Docker network
docker network create my-app-network

#Run a MySQL container on the custom network
docker run -d --name mydb --network my-app-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8
With that we created this database in our myapp network

Then finally run as a container
#Run a Flask container on the custom network, mapping port 5002 and using the specified image
docker run -p 5002:5002 --network my-app-network 043309335662.dkr.ecr.us-east-1.amazonaws.com/ecr-flask-mysql:latest - docker run then the port 5002 in the container and 5002 on our local machine, then our custom network followed by the url.

#### Using Docker Compose to run the image we pull from ECR as a container
version: '3.8' #The version tells docker compose which version of the file format we're using 

<br> services: #The services is where we list all the different parts of our app, which is the web service(our flask application) and a database
<br>   web:
<br>   image: 043309335662.dkr.ecr.us-east-1.amazonaws.com/ecr-flask-mysql:latest  #Instead of building the image locally we are going to replace it with image and paste our ecr repository
<br>    ports:
<br>     - "5002:5002" #We set the ports to 5002 for the web service
<br>   depends_on:
<br>     - mydb  #This line means that the web service depends on the database service, so docker compose will start the database service first before starting the web service

<br> db:
<br>   image: mysql:8 #We are using an image we found online, this tells docker compose which image version we're using
<br>   environment:
<br>   MYSQL_ROOT_PASSWORD: my-secret-pw  #We set the environment variable mysql root password which we set to my secret pw

Then do docker-compose up

Successfully used docker compose to manage a multi container application using an image we pulled from AWS ECR 

### Important Docker Commands to know!
These commands will help you keep your docker environments clean, organised and running smoothly especially as you start working with more images and containers in your projects.

docker images - It will give you all the images that you have stored locally, it will display a list of all the docker images on the system, including details like the repository name, the version, the id, when it was created and the size. Useful to see which images are available and which you would like to clean up.

docker inspect imageid (You can use the docker images command to see the imageid) - Gives us the details about the image 

docker rmi imageid - Used to remove images that you no longer need, if an image is still being used by a container docker won't remove it and you will need to stop and remove the container first.

docker system prune - Removes all unused images, all networks not used by at least one container in one go, useful for clearing out resources that are no longer needed. 

docker ps - Shows you the containers that are currently running
docker ps -a - Shows you all of the containers including the ones not in use.

docker stop containerid - Stops running containers, but doesn't remove them.
docker rm containerid - Removes containers

If you are trying to make an image from a docker file but it is the second dockerfile you've made that you're trying to a make an image from use this command
docker build -f TheSecondDockerfile.YouMade -t imagename .

### Making Our Image Lighter: Multistage Builds
Large images can slow down deployments, it consumes more bandwidth and requires more storage.
We will be learning how to optimise our docker file using multistage builds.

What are multistage builds? - Multistage builds in docker allow you to use multiple from statements in your docker file.
The idea of a multi stage build using from statements is to use one stage to build your application and another much lighter stage to create the final image that you actually deploy.

There's a part that requires all the dependencies to build the application, but all those dependencies are not then required in the actual final image.
This lets you discard any unnecessary files and dependencies resulting in a much smaller optimised image.

Docker file

#Stage 1: Build Stage

FROM python:3.8-slim as build 

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

COPY . . 
#The first . is to say what files in our current directory we want to copy, the second . is where in our container do we want to store it, referring to the  /app directory cos once we set the work directory our , becomes the app directory

RUN pip install flask mysqlclient

#Stage 2: Production Stage

FROM python:3.8-slim

WORKDIR /app

COPY --from=Build /app /app
#Means we're only going to copy the necessary files from the build stage, we specify app as that's where the file is stored
EXPOSE 5002

CMD ["python", "app.py"]

The file size has decreased because we removed all the build tools and only kept what's needed for the runtime environment

### Advanced Topic Overview
As you start working with larger applications or deploying your services in production, managing your individual containers manually becomes increasingly challenging. Even if you have to use docker compose it's still challenging because you would be dealing with hundreds of containers.

This is where advanced tools like Kubernetes and Docker Swarm come in to play.
These tools are essential for automating, scaling and managing containerised applications in production environments.

#### Brief Kubernetes Introduction
What is Kubernetes(sometimes known as K8's) - Kubernetes is an open source platform designed to automate the deployment, scaling and operation of application containers. 

It takes container management to the next level by providing advanced features like container orchestration, automatic scaling and self-healing. These features ensure that your application runs smoothly and efficiently, no matter the scale. 

How does Kubernetes actually help? - It helps solve the challenges that arise when you move beyond a handful of containers on a single machine like we've been doing in this section, to managing a fleet of containers across multiple machines.

It abstracts the underlying infrastructure allowing you to focus more on your application rather than the intricacies of managing individual containers. Meaning developers want to focus on application code, all these tools help developers do that because it manages all of this for them.

#### Docker Swarm vs Kubernetes

Docker swarm is docker's native clustering and orchestration tool built into docker, which means it's very easy to set up and use, especially if you're already familiar with docker's commands and environments

Kubernetes is a more complex and feature rich container orchestration platform, it was originally developed by google, it has become the industry standard for managing containers at scale. Kubernetes offers greater flexibility and scalability which is essential for large scale enterprise level deployments.

Key features of Docker Swarm and Kubernetes

Docker Swarm                                    |      Kubernetes
1. No Auto Scaling                                1. Auto Scaling
Docker swarm does not have built in auto scaling    Kubernetes has built-in autoscaling features
capabilities which means you'll need to manage      allowing your applications to automatically 
scaling manually or through external tools         scale up or down based on demand which is 
                                                   critical for handling fluctuating workloads.
2. Good Community                                 
It has a good community while not as large as   |  2. Great Active Community
kubernetes, docker swarm has a solid community       It's community is much better than docker 
that supports it.                                    swarm because the community is vast and                                                         active, which means better suppport, more
                                                     resources and continuous improvements.
3. Easy to start a Cluster                      | 3. Difficult to start a cluster
It's easier to start a cluster which is one of        While kubernetes offers a lot of power,
docker swarms biggest strengths, starting a swarm     it's also more challenging to set up.
cluster is simple and integrates seamlessly with     Starting a kubernetes cluster requires a 
existing docker setups.                              deeper understanding of the tool and its
                                                     concepts
4. Limited to the Docker API's Capabilities     |  4.Not Limited to the Docker API's Capabilities
                                                   This means it can work with a wider range of
                                                   container runtimes and offers more advanced                                                     features for managing complex applications

So in summary
<br> Docker Swarm is easier to use and integrates seamlessly with Docker, making it a great option for smaller, less complex deployments.
<br> However, Kubernetes offers more power, flexibility, and scalability, making it the preferred choice for large-scale enterprise-level applications.

#### Why Should You Use Orchestration Tools?
Orchestration tools are designed to help you manage large scale deployments and ensure that your application runs smoothly across multiple environments.

Manage Large Scale Deployments
Orchestration tools like Kubernetes and Docker Swarm are built to handle large numbers of containers spread across multiple machines. This makes it easier to manage complex environments by automating the deployment operation and scaling of contaniners

Ensure High Availability for Your Applications
They automatically monitor the state of your containers and can restart or relocate them in case of failure. This ensures that your applications remain available and can recover from failures without manual intervention.

Automate Scaling and Recovery 
These tools can automatically scale your applications up or down based on demand, which is crucial for maintaining performance during peak times and saving resources during lower usage periods. Additionally, they offer self-healing capabilities by detecting and restarting failed containers, ensuring continuous service.

You can also 
simplify complex deployments, enhance reliability and improve resource utilisation 









