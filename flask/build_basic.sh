#!/bin/bash

tar -cvf ./basic.tar ./basic
gzip -v ./basic.tar
mv ./basic.tar.gz ./docker/app

