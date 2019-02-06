#!/usr/bin/bash

while getopts n:l: option
do
case "${option}"
in
l) LOCATION=${OPTARG};;
n) NAME=${OPTARG};;
esac
done
mkdir ./src/
docker-compose run web django-admin.py startproject $NAME ./src/
