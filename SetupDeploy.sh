#! /bin/sh 
git clone --recursive https://github.com/tensorflow/serving
cd serving

sudo docker build --pull -t $USER/tensorflow-serving-devel -f tensorflow_serving/tools/docker/Dockerfile.devel .
