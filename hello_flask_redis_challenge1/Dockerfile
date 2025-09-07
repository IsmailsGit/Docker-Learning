FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install redis
EXPOSE 5000
CMD ["python", "app.py"]