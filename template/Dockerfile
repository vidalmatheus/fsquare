FROM python:3.10-slim

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    echo "export LS_OPTIONS='--color=auto'" >>~/.bashrc && \
    echo "eval "\`dircolors\`"" >>~/.bashrc && \
    echo "alias ls='ls \$LS_OPTIONS'" >>~/.bashrc && \
    echo "alias ll='ls \$LS_OPTIONS -l'" >>~/.bashrc && \
    echo "alias l='ls \$LS_OPTIONS -lA'" >>~/.bashrc

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        vim \
        wait-for-it \
        curl \
        jq \
        locales \
        supervisor \
        libmagic-dev \
        build-essential \
        gcc libmemcached-dev zlib1g-dev \
        libgeos-dev \
        git \
        nodejs \
        npm && \
    pip install uwsgi uwsgitop && \
    apt-get purge -y build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /dkdata
WORKDIR /app


COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY frontend/package.json frontend/package.json
COPY frontend/package-lock.json frontend/package-lock.json
RUN cd frontend && npm install && npm install -g pm2
COPY frontend frontend
RUN cd frontend && npm run build

ENV PYTHONUNBUFFERED=1 \
    NODE_ENV=production \
    API_MOCK=0 \
    PYTHONIOENCODING=UTF-8 \
    LANG=en_US.UTF-8 \
    DJANGO_STATIC_ROOT=/dkdata/static \
    DJANGO_LOG_FILE=/dkdata/{{name}}.log \
    UWSGI_PROCESSES=3 \
    PORT=3000 \
    HOST=0.0.0.0 \
    API_BASE_URL=http://localhost:8000

COPY . /app
COPY docker/bin/* /usr/bin/
COPY docker/compose/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY docker/compose/nginx/proxy_params /etc/nginx/proxy_params
