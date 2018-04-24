#! /bin/sh 
chmod +x *.sh
./Ubuntu_Install_Depends.sh
./SetupProject.sh
./GenerateMLModes.sh
./RunMLModelServer.sh
