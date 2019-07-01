#!/bin/sh

VIDEO_PATH_DEFAULT=/data/video.mp4
STREAM_LOOP_DEFAULT=1

# check if feed url is configured
if [[ -z "${FEED_URL}" ]]; then
    echo "Environment variable \$FEED_URL is required, but it's not configured";
    exit 1;
fi

# check if video path is configured
if [[ -z "${VIDEO_PATH}" ]]; then
    echo "Environment variable \$VIDEO_PATH is not configured. Using default value (${VIDEO_PATH_DEFAULT})";
    VIDEO_PATH=$VIDEO_PATH_DEFAULT
fi

# check if stream loop is configured
if [[ -z "${STREAM_LOOP}" ]]; then
    echo "Environment variable \$STREAM_LOOP is not configured. Using default value (${STREAM_LOOP_DEFAULT})";
    STREAM_LOOP=$STREAM_LOOP_DEFAULT
fi

sleep 1;

for i in `seq $STREAM_LOOP`; do
    echo "running [$i/$STREAM_LOOP]: ffmpeg -re -i $VIDEO_PATH $FEED_URL";
    ffmpeg -re -i $VIDEO_PATH $FEED_URL; 
done;