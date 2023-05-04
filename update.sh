git pull --force
source .venv/bin/activate
pip install -r requirements.txt -U
deactivate
sudo chown www-data:www-data -R .
sudo systemctl daemon-reload
sudo service edisubot restart