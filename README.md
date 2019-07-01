# Camera Kafka Producer

Este projeto é um script feito em python para publicar os frames produzidos por uma ou mais câmeras em um tópico do kafka.

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

### Obter mais informações

Para obter mais informações, utilize o comando abaixo.

```bash
./capture --help
```

### Testando o ambiente

Para testar o ambiente, vamos transmitir um vídeo de um arquivo local. Dentro da raiz do projeto, utilize o comando abaixo para fazer o download de um vídeo exemplo.

```bash
mkdir -pv data
wget file-examples.com/wp-content/uploads/2017/04/file_example_MP4_1280_10MG.mp4 -O data/video.mp4
```

Após isso, utilize o comando abaixo para iniciar os serviços.

```bash
docker-compose up
```

## Links utilizados

* [Distributed Video Streaming with Python and Kafka](https://medium.com/@kevin.michael.horan/distributed-video-streaming-with-python-and-kafka-551de69fe1dd)
