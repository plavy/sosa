FROM python

ENV ROOT_PASSWORD=123

RUN pip install bandit

WORKDIR /app

ADD . .

CMD ["/bin/bash", "run.sh"]