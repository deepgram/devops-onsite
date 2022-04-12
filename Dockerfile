FROM python:3.11-rc-alpine3.14
LABEL maintainer="Adam J. Sypniewski <adam@deepgram.com>"

WORKDIR /usr/src/app

COPY . .

RUN pip install .

ENTRYPOINT ["gram"]
