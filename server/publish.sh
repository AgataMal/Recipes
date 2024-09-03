#!/bin/bash

docker build -t recipes .
docker tag recipes agatamalczyk/recipes:v1.1
docker push agatamalczyk/recipes:v1.1
