#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
#COPY ./requirements.txt /app/requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#COPY ./app /app/app
FROM python:3.9
LABEL maintainer="Eungoo Jung <akasilvernine@gmail.com>"
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
#CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
