#!/bin/bash

wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.31.0-linux64.tar.gz -O > /usr/bin/geckodriver'
sudo chmod +x /usr/bin/geckodriver
rm geckodriver-v0.31.0-linux64.tar.gz
