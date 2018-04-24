#! /bin/sh 
cd stock-data-neural-network-predictor
chmod +x ./BuildModels.sh
./BuildModels.sh
cd ..
cd stock-data-SVM-predictor
chmod +x ./BuildModels.sh
./BuildModels.sh
cd ..



