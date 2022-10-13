FROM python:3

WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]