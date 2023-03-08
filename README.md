# inlookads



source env/bin/activate
python3 manage.py runserver

source env/bin/activate
python3 manage.py tailwind start

python3 manage.py makemigrations    
python3 manage.py migrate 
python3 manage.py createsuperuser
python3 manage.py runserver  

env\Scripts\activate   
python manage.py runserver  
