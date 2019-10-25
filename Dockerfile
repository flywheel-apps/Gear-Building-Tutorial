FROM alpine:latest
RUN apk add --update \
    python \
    py-pip \
  && pip install flywheel-sdk \
  && rm -rf /var/cache/apk/*
ENTRYPOINT ["python run.py"]
