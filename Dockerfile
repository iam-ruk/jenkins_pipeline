FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    libmariadb-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]