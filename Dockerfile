FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /goodbuy-django-docker
WORKDIR /goodbuy-django-docker

# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt /goodbuy-django-docker/
RUN pip install -r requirements.txt

COPY . /goodbuy-django-docker/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]