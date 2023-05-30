FROM python

RUN pip install bandit

WORKDIR /app

ADD . .

CMD ["/bin/bash", "run.sh"]