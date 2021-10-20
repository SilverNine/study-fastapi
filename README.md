# env

virtualenv -p python3 ~/python-env/981park-operation-know

source ~/python-env/981park-operation-know/bin/activate

# first init

pip3 install fastapi

pip3 install 'uvicorn[standard]'

pip3 install gunicorn

pip3 freeze > requirements.txt

# init

pip3 install -r requirements.txt

# local - start app

uvicorn main:app --reload --host 0.0.0.0 --port 8000

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080
