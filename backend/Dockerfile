FROM python:3.10-slim
WORKDIR /app

# curl нужен для healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# авто-reload (как у тебя уже)
RUN pip install --no-cache-dir watchdog

COPY app.py .

EXPOSE 5000
CMD ["watchmedo", "auto-restart", "--patterns=*.py", "--recursive", "--", "python", "app.py"]

