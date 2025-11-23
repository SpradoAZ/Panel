# dependencias
python -m venv env
.\env\Scripts\activate
pip install flask
pip install pymysql
pip install flask flask-sqlalchemy flask-migrate pymysql
pip install Flask-Migrate
python .\main.py 

**nombre de BD**
datos_cohete

# migraciones
flask db init
flask db migrate
flask db upgrade