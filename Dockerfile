FROM balenalib/raspberry-pi-debian-python:latest

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./app

CMD [ "python", "./app/webapi.py" ]