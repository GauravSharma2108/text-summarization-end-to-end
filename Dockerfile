FROM python:3.11-slim-buster
WORKDIR /app
RUN apt-get update && apt-get install -y gcc python3-dev
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]