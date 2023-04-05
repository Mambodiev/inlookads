cd djvideomem
source env/bin/activate
python3 manage.py tailwind start

cd djvideomem
source env/bin/activate
python3 manage.py runserver 

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

python manage.py makemigrations    
python manage.py migrate 
python3 manage.py createsuperuser
python3 manage.py runserver  


git init
git add .
git commit -m "filter by category with success"
git push