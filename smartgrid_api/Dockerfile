# Dockerfile for Django backend
FROM python:3.11-slim
# NOTE: This image may contain vulnerabilities. Consider using a more up-to-date or minimal base image and regularly update dependencies.

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "smartgrid_api.wsgi:application", "--bind", "0.0.0.0:8000"]
