FROM python:3.11-alpine

RUN apk update \
    && apk add gcc g++ python3-dev musl-dev
RUN apk add libffi-dev
RUN pip install --upgrade pip

WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
COPY . .

RUN python manage.py makemigrations && python manage.py migrate 
RUN  python manage.py collectstatic --no-input
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "15" ,"gymkhana_portal.wsgi"]
# CMD ["python3","manage.py","runserver"]
