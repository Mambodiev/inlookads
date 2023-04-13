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
M@diev2022
python manage.py makemigrations    
python manage.py migrate 
python3 manage.py createsuperuser
python3 manage.py runserver  


git init
git add .
git commit -m "privacy page"
git push

youtube-dl  -f 22 --no-playlist  -o  "~/home/diev/Videos/Django/django Yuksel/%(title)s.%(ext)s" "https://www.youtube.com/watch?v=6RR8WrvshQA&list=PLIUezwWmVtFXaHcJ63ZM6uOJdhMrnZFFk&index=2&pp=iAQB"