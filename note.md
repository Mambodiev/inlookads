
source env/bin/activate
python3 manage.py runserver 


python3 manage.py tailwind start


python manage.py makemigrations    
python manage.py migrate 
python3 manage.py runserver 

python manage.py makemigrations    
python manage.py migrate 
python3 manage.py createsuperuser
python3 manage.py runserver  


git init
git add .
git commit -m "google account authentification"
git push