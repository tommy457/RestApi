FROM python:3.7-alpine
LABEL maintainer "tommy457"

ENV PYTHONUNBUFFERED 1

WORKDIR /app


COPY ./requirements.txt /tmp

COPY ./app /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        tommy

ENV PATH="/py/bin:$PATH"

USER tommy
