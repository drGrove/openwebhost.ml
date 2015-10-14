FROM debian:jessie

ENV LC_ALL=C
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
	( apt-get install -y \
		git \
		python-dev \
		python-pip \
		build-essential \
		libssl-dev || \
	apt-get install -y \
			git \
			python-dev \
			python-pip \
			build-essential \
			libssl-dev \
	) && \
	apt-get clean && \
	rm -rf /tmp/* /var/tmp/*

ADD ./ /opt/app/
WORKDIR /opt/app
RUN sh setup.sh

CMD ["python2.7", "main.py"]
