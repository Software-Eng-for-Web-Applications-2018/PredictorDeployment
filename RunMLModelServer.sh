#! /bin/sh 
cd stock-data-neural-network-predictor
sh ./RunModelServer.sh &
cd .. 
cd stock-data-SVM-predictor
sh ./RunModelServer.sh &
cd .. 



