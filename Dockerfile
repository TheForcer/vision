FROM python:3.7-slim

LABEL name="vision"
LABEL authors="Felix"
LABEL description="Small python matrix-bot for a couple of small tasks"

ADD . /opt/
VOLUME [ "/opt/python-scripts", "/opt/scripts", "/opt/config" ]

RUN pip install -r /opt/requirements.txt && \
    mkdir /opt/data

CMD [ "python3", "/opt/vision-bot.py" ]