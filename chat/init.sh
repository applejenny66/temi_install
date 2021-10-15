#!/bin/bash
GREEN='\033[0;32m'
PURPLE='\033[0;35m'
NC='\033[0m'

sudo apt-get install libncurses5-dev libncursesw5-dev
sudo apt install git
sudo apt install make
sudo apt install build-essential


sudo -H pip3 install --upgrade pip
echo "${PURPLE}install mysql-server${NC}"
sudo apt-get install mysql-server
echo "${GREEN}[OK]${NC}"
echo "${PURPLE}install mysql-client${NC}"
sudo apt install mysql-client
echo "${GREEN}[OK]${NC}"
echo "${PURPLE}install libmysqlclient-dev${NC}"
sudo apt install libmysqlclient-dev
echo "${GREEN}[OK]${NC}"

sudo apt-get install net-tools
sudo netstat -tap | grep mysql