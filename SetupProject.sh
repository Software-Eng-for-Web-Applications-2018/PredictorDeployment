#! /bin/sh 
git clone https://github.com/Software-Eng-for-Web-Applications-2018/stock-data-site.git
git clone https://github.com/Software-Eng-for-Web-Applications-2018/stock-data-feed.git
git clone https://github.com/Software-Eng-for-Web-Applications-2018/PredictorDeployment.git
git clone https://github.com/Software-Eng-for-Web-Applications-2018/stock-data-SVM-predictor.git
git clone https://github.com/Software-Eng-for-Web-Applications-2018/stock-data-neural-network-predictor.git


#Install Ubuntu Depends

chmod +x stock-data-site/Ubuntu_Install_Depends.sh
chmod +x PredictorDeployment/Ubuntu_Install_Depends.sh
chmod +x stock-data-neural-network-predictor/Ubuntu_Install_Depends.sh

sh stock-data-site/Ubuntu_Install_Depends.sh
sh PredictorDeployment/Ubuntu_Install_Depends.sh
sh stock-data-neural-network-predictor/Ubuntu_Install_Depends.sh

sudo -H pip3 install -r stock-data-site/requirements.txt
sudo -H pip3 install -r stock-data-feed/requirements.txt
sudo -H pip3 install -r stock-data-neural-network-predictor/requirements.txt
sudo -H pip3 install -r stock-data-SVM-predictor/requirements.txt
