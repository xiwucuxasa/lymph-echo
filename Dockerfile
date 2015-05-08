FROM python:2.7.6

ADD . /lymph-echo

WORKDIR lymph-echo/

RUN pip install -r requirements.txt

CMD lymph node --guess-external-ip
