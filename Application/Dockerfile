FROM python:3.8.10-alpine

LABEL maintainer="aleksey.eronin96@gmail.com"

ENV API_KEY="your_api_key"
ENV MY_NAME="Aleksey"
ENV COUNTRY="RU"

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app

ENTRYPOINT [ "python" ]

CMD [ "./app.py" ]
