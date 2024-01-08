FROM python:3.11-alpine

RUN apk update \
    && apk add gcc g++ python3-dev musl-dev
RUN apk add libffi-dev
RUN pip install --upgrade pip

WORKDIR /app
COPY ./requirements_prod.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
COPY . .

CMD ["sh","scripts/migrate_and_run"]
# CMD ["python3","manage.py","runserver"]
