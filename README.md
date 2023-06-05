# hw_10_web

1) Create a project: django-admin startproject some_name
2) After start this command we need to set both urls.py -- start app by: python manage.py startapp polls
3) Then we need to start server python manage.py runserver
4) To synchronize the camp of the models in Python and the table in the database, 
     it is enough to run the command : python manage.py migrate
5) python manage.py makemigrations polls 
6) to make migration : python manage.py migrate 
7) Щоб користуватися адміністративною панеллю Django,
       потрібно спочатку створити користувача, який зможе зайти в адмін панель: python manage.py createsuperuser
        http://127.0.0.1:8000/admin/
