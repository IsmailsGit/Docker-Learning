#We use the python image and the version
FROM python:3.8-slim
#We are setting the work directory so that any commands after this will be run in this directory
WORKDIR /app
#We are going to copy all of the files from our current directory
COPY . .
#RUN apt-get update && apt-get install -y
#gcc
#python3-dev
#libmariadb-dev
#pkg-config
#We install flask
RUN pip install flask redis
#We expose port 5002, we are making this port available so we can access the container from our local host, this makes the application accessible from outside the container
EXPOSE 5000
#The cmd command tell docker to run our python application
CMD ["python", "app.py"]