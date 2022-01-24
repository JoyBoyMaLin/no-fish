FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN echo "UTC" >  /etc/timezone

RUN apt-get update && apt-get install -y build-essential musl-dev gettext default-libmysqlclient-dev \
        --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip3 install poetry

RUN adduser --system --group hundun

RUN set -ex && mkdir /fish
WORKDIR /fish

COPY pyproject.toml poetry.lock /fish/
RUN set -ex && POETRY_VIRTUALENVS_CREATE=false poetry install --no-dev --no-root

COPY scripts/ /
RUN chmod +x /*.sh
RUN chown hundun:hundun /*.sh

COPY fish /fish
RUN chown -R hundun:hundun /fish

USER hundun

EXPOSE 8000

ARG git_revision_id
ENV GIT_REVISION_ID ${git_revision_id}


CMD ["/start.sh"]
