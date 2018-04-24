#! /bin/sh 
#sudo apt install docker.io
sudo apt-get update && sudo apt-get install -y build-essential curl libcurl3-dev git libfreetype6-dev libpng12-dev libzmq3-dev pkg-config python-dev python-numpy python-pip software-properties-common swig zip zlib1g-dev
sudo pip install grpcio

#sudo pip install tensorflow-serving-api
sudo -H pip install tensorflow-serving-api-python3

#Copy over files to be able to run the code in python 3.5. Very stupid
sudo cp -r /usr/local/lib/python2.7/dist-packages/tensorflow_serving /usr/local/lib/python3.5/dist-packages/tensorflow_serving 
sudo cp -r /usr/local/lib/python2.7/dist-packages/tensorflow_serving_api-1.7.0.dist-info /usr/local/lib/python3.5/dist-packages/tensorflow_serving_api-1.7.0.dist-info

echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add -

sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y

sudo apt update

sudo apt-get install libstdc++6

#wget http://storage.googleapis.com/tensorflow-serving-apt/pool/tensorflow-model-server-1.5.0/t/tensorflow-model-server/tensorflow-model-server_1.5.0_all.deb
#sudo dpkg -i tensorflow-model-server_1.5.0_all.deb
sudo apt-get install tensorflow-model-server


