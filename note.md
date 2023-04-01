

source env/bin/activate
python3 manage.py tailwind start

source env/bin/activate
python3 manage.py runserver 

{% comment %} {% endcomment %}  
python manage.py makemigrations    
python manage.py migrate 
python3 manage.py runserver 

python manage.py makemigrations    
python manage.py migrate 
python3 manage.py createsuperuser
python3 manage.py runserver  


git init
git add .
git commit -m "partially added addd to cart or add to favorite functionality "
git push