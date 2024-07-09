FROM python:3.9

RUN pip install pandas

WORKDIR /app

COPY example.py example.py

ENTRYPOINT ["python", "example.py"]  