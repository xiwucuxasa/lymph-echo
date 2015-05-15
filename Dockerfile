FROM python:2.7.7

ADD . /lymph-echo

WORKDIR lymph-echo/

RUN pwd

RUN ls -lah

RUN pip install -r requirements.txt

CMD lymph node --guess-external-ip
