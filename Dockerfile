FROM python:3.11-slim

WORKDIR /app

COPY calculator ./calculator
COPY test ./test
COPY main.py .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

RUN pytest test/test_calculator.py

CMD ["python", "main.py"]