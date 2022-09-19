# r-telecom_test_task

### This project is test task for R-Telecom company

# Setup:
### Create Python virtual environment 
```
python3 -m venv venv
```
### Activate it
```
. venv/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```

### Fill configuration in .env:
```
cp .env-example .env
```
### Run server:
```
python3 main.py
```

# Setup with Docker:
### Run:
```
docker-compose up --build
```

# API Documentation:
### Follow the link when the server is running:
http://localhost:8000/docs/
