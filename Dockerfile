FROM debian:jessie

ENV LC_ALL=C
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
	apt-get install -y \
		python \
		openssl \
		python-flask \
		python-mysqldb && \
	apt-get clean && \
	rm -rf /tmp/* /var/tmp/*

ADD ./ /opt/app/
WORKDIR /opt/app

CMD ["python2.7", "main.py"]
