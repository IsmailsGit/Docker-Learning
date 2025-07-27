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

# Stage 2: Production Stage

FROM python:3.8-slim

WORKDIR /app

COPY --from=Build /app /app
#Means we're only going to copy the necessary files from the build stage, we specify app as that's where the file is stored
EXPOSE 5002

CMD ["python", "app.py"]
