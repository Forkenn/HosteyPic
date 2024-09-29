FROM python:3.12-alpine3.20


ENV LANG=C.UTF-8

RUN apk update
RUN apk add --no-cache python3-dev libstdc++ && \
    apk add --no-cache g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h 
RUN apk add libxml2-dev libxslt-dev
RUN apk add gcc musl-dev libffi-dev
RUN mkdir -p /src/app
RUN mkdir -p /src/app/hosteypic_server
WORKDIR /src/app

#ENV PYTHONPATH=/src/app:/src/app/source

COPY poetry.lock pyproject.toml ./
COPY hosteypic_server ./hosteypic_server

RUN pip install --no-cache-dir poetry==1.8.3 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

#CMD ["uvicorn", "hosteypic_server.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["sleep", "60"]