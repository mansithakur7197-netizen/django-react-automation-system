# empty - run makemigrations locally
backend/# optional: create virtualenv
python -m venv .venv
# activate:
# Linux/Mac: source .venv/bin/activate
# Windows: .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
# edit .env if you want MySQL; default is sqlite for local
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py fetch_data   # test command to populate datapoint
python manage.py runserver 0.0.0.0:8000
python manage.py test
