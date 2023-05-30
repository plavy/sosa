FROM python

RUN pip install bandit

WORKDIR /app

ADD . .

# Unittest run and save logs
RUN python -m unittest

# Bandit run and save logs
RUN bandit -r .