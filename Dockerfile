FROM python:3.7
LABEL maintainer="artemzraev@gmail.com"
COPY . /animal_classification
WORKDIR /animal_classification
RUN pip install -r requirements.txt
EXPOSE 8180
EXPOSE 8181
VOLUME /animal_classification/animal_classification/models
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
