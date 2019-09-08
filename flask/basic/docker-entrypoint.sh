#!/bin/bash

service nginx start
uwsgi --ini ./app.ini