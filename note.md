cd realadsnow
source env/bin/activate
python3 manage.py tailwind start

cd realadsnow
source env/bin/activate
python3 manage.py runserver 


{% translate "" %}

cd Videos
cd Matts
cd Build_a_Dynamic_Filter_Form
cd djfilter
cd src
source env/bin/activate
python3 manage.py runserver 

{% comment %} {% endcomment %}  

python manage.py makemigrations    
python manage.py migrate 
python3 manage.py runserver 
M@diev2022
python manage.py makemigrations    
python manage.py migrate 
python3 manage.py createsuperuser
python3 manage.py runserver  


git init
git add .
git commit -m "START MODEL TRANSLATION ACORDING TO YUKSEL"
git push
Gray-900
#111827

display: none!important;


django-admin makemessages --all --ignore=env
django-admin compilemessages --ignore=env