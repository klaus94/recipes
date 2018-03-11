# kill python server
sudo lsof -t -i tcp:5000 -s tcp:listen | sudo xargs kill

# kill angular server
sudo lsof -t -i tcp:4200 -s tcp:listen | sudo xargs kill
