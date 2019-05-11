FROM python:3.7-slim

ADD vision-bot.py /opt/

RUN pip install requests && \
    pip install matrix_client && \
    pip install configparser && \
    mkdir /opt/data

VOLUME [ "/opt/python-scripts", "/opt/scripts", "/opt/vision.cfg" ]

CMD [ "python", "/opt/vision-bot.py" ]