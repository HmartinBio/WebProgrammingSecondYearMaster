#!/bin/bash 

mkdir -p $HOME/Software
wget https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli-linux-x64.tar.gz -O $HOME/Software/heroku.tar.gz
cd $HOME/Software
tar xvfz heroku.tar.gz
rm heroku.tar.gz
export PATH=${PATH}:${HOME}/Software/heroku-cli-v6.15.24-e5de04c-linux-x64/bin
source ~/.bashrc
