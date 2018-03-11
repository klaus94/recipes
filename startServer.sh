# start backend-server
cd recipes-server
python app.py&
cd ..

# start frontend-server
cd recipes-client
ng serve --host 0.0.0.0&
cd ..
