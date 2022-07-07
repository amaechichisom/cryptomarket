FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1\
     PYTHONUNBUFFERED=1

WORKDIR /usr/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /usr/app

CMD [ "python", "index.py" ]