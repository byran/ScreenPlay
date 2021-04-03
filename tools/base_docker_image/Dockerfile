FROM ubuntu:20.04
LABEL maintainer="Byran Wills-Heath"

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		python3 \
		python3-pip \
		python3-venv \
		wget \
		curl \
		make \
	&& rm -rf /var/lib/apt/lists/*

RUN useradd -m --uid 1001 user
USER user
WORKDIR /home/user

RUN mkdir -p /home/user/.local/bin/
ENV PATH="/home/user/.local/bin:${PATH}"
