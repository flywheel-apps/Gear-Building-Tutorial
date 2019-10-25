FROM alpine:latest
RUN apk add --no-cache bash \
    --update \
    python \
    py-pip \
  && pip install flywheel-sdk \
  && rm -rf /var/cache/apk/*
ENTRYPOINT ["python run.py"]
