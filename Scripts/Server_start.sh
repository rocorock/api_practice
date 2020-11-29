#!/bin/bash
sudo chmod 777 ~/Database
sudo chmod 777 ~/Database/Address.sqlite
touch sample.txt
python3 ~/src/app/rest_app.py
python3 ~/src/app/rest_api.py
