#!/bin/bash

docker run -d \
-p 8080:8080 \
--name myapp \
myapp:latest
