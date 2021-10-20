# env

virtualenv -p python3 ~/python-env/study-fastapi
source ~/python-env/study-fastapi/bin/activate

# first init

pip install fastapi
pip install 'uvicorn[standard]'
pip freeze > requirements.txt

# init

pip install -r requirements.txt

# start app

uvicorn main:app --reload
