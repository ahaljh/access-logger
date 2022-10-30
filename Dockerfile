FROM python:3.10-slim-buster
LABEL maintainer="gardenc.org@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV WORKSPACE /workspace/

COPY ./ /code/

RUN pip3 install --no-cache-dir -r /code/requirements.txt

RUN mkdir /workspace
WORKDIR /workspace/

EXPOSE 8000
CMD ["/bin/bash", "/code/entrypoint.sh"]
