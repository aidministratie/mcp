FROM python:3.12-slim

WORKDIR /app

COPY bridge.py .
COPY pyproject.toml .
COPY README.md .

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "bridge.py"]
