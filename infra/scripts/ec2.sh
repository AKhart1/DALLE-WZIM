#!/bin/bash

sudo apt-get update
sudo apt-get install git -y
cd /home/ubuntu
git clone https://github.com/AKhart1/DALLE-WZIM.git
sudo apt-get install python3-pip -y
cd DALLE-WZIM/
pip install -r requirements.txt --break-system-packages
cd app/
python3 app.py

