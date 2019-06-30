# Camera Publisher

## Pré-requisitos

* python 3.6+

### Bibliotecas

* argparse
* cv2
* kafka

## Como utilizar

### Publicando o vídeo

#### Única câmera

Para publicar o vídeo de uma câmera, é preciso especificar os seguintes parâmetros.

* Url de origem do vídeo - `-s` ou `--source-input`;
* Url do servidor onde o kafka está funcionando - `-d` ou `--kafka-url`;
* Tópico para publicar os frames da câmera - `-t` ou `--kafka-topic`.

##### Exemplo

```bash
./capture.py \
-s http://192.168.100.15/stream \
-d localhost:29092 \
-t kafka-python-topic
```

#### Múltiplas câmeras

O argumento `--camera-source` ou `-s` suporta múltiplas urls separadas por vírgula.

##### Exemplo

```bash
./capture.py \
-s http://192.168.100.15/stream,http://192.168.100.20/stream \
-d localhost:29092 \
-t kafka-python-topic
```

### Mais informações

Para obter mais informações, utilize o comando abaixo.

```bash
./capture --help
```

## Links utilizados

* [Distributed Video Streaming with Python and Kafka](https://medium.com/@kevin.michael.horan/distributed-video-streaming-with-python-and-kafka-551de69fe1dd)
