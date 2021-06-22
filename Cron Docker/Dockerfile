# syntax=docker/dockerfile:1

FROM ubuntu

WORKDIR /home

COPY requirements.txt requirements.txt
COPY dashboard.py dashboard.py
COPY run.py run.py
RUN  apt-get update &&  apt-get upgrade
RUN  apt-get install -y cron
RUN  apt-get install -y  python3
RUN  apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
RUN apt-get install -y vim

ADD crontab /etc/cron.d/test
RUN chmod 0644 /etc/cron.d/test
RUN crontab /etc/cron.d/test
RUN touch /var/log/cron.log
#CMD ["service", "cron", "start"]

ADD cron.sh /home/cron.sh
RUN chmod +x /home/cron.sh
ENTRYPOINT ["bash","/home/cron.sh"]

EXPOSE 8000

CMD ["python3", "/home/run.py"]
