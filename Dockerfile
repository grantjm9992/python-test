FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/app

EXPOSE 8000

ENV PATH="/app/venv/bin:$PATH"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
