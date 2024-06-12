FROM python:3.9-alpine

WORKDIR /usr/local/share/

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps build-base \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps build-base

COPY ./app ./app

CMD [ "python" ,"app" ]