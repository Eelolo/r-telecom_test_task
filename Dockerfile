FROM python:3.9

RUN mkdir -p r-telecom_test_task
WORKDIR r-telecom_test_task

COPY . .

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ['python3', 'main.py']