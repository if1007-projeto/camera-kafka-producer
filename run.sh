#!/bin/bash

# check if camera urls is assigned
if [[ -z "${SOURCE_URLS}" ]]; then
    echo "Environment variable \$SOURCE_URLS is required, but has no value.";
    exit 1;
fi

# check if kafka url is assigned
if [[ -z "${KAFKA_URL}" ]]; then
    echo "Environment variable \$KAFKA_URL is required, but has no value.";
    exit 1;
fi

# check if kafka topic is assigned
if [[ -z "${KAFKA_URL}" ]]; then
    echo "Environment variable \$KAFKA_TOPIC is required, but has no value.";
    exit 1;
fi

python ./capture.py -s $SOURCE_URLS -d $KAFKA_URL -t $KAFKA_TOPIC