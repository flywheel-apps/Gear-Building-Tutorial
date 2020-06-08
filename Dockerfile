FROM alpine:latest
RUN apk add --no-cache bash \
    --update \
    python3 \
    py-pip \
  && pip install flywheel-sdk \
  && rm -rf /var/cache/apk/*

ENV FLYWHEEL=/flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY run.py ${FLYWHEEL}/run.py

ENTRYPOINT ["python3 run.py"]
