FROM python:3.8.5

WORKDIR /app
ARG TARGET_BRANCH
ARG IMAGE_RECOGNITION_MODEL
ENV DEPLOYMENT=local

RUN apt-get update \
&& apt-get -y install git \
&& git clone https://github.com/toposoid/toposoid-common-image-recognition-web.git \
&& cd toposoid-common-image-recognition-web \
&& git fetch origin ${TARGET_BRANCH} \
&& git checkout ${TARGET_BRANCH} \
&& pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt \
&& python downloadModel-${IMAGE_RECOGNITION_MODEL}.py


COPY ./docker-entrypoint.sh /app/
ENTRYPOINT ["/app/docker-entrypoint.sh"]
