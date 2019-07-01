FROM denismakogon/opencv3-slim:edge

WORKDIR /usr/src/app

ENV SOURCE_URLS=http://localhost:8090/stream
ENV KAFKA_URL=localhost:32181
ENV KAFKA_TOPIC=meu-topico-legal


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN rm -fr ~/.cache/pip /tmp*

COPY . .

ENTRYPOINT [ "./run.sh" ]