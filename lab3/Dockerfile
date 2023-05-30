FROM python

ENV ROOT_PASSWORD=123456

RUN pip install bandit pylint

WORKDIR /app

ADD . .

CMD ["/bin/bash", "run.sh"]