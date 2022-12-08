FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /goodbuy-django-docker
WORKDIR /goodbuy-django-docker
COPY requirements.txt /goodbuy-django-docker/
RUN pip install -r requirements.txt
COPY . /goodbuy-django-docker/
EXPOSE 8000