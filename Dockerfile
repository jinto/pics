FROM python:3.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /src

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
