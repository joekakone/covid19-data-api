# Covid19 Data API
Hello, I'm [Joseph Konka](https://www.linkedin.com/in/joseph-koami-konka/), Python enthousiast. In this porject, I'm building an API with Flask to provide covid19 data for my dashboard. You can see the result [here](https://covid19data-jk.herokuapp.com/)

This API returns data about covid19 deseases:
1. ECOWAS
2. World

## Setup environment
```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=app
```

## Launch
```sh
python3 app.py
flask run --host=0.0.0.0 --port=5000
gunicorn app:app
```
