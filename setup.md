## setup

#prerequisites:
- python installed
- pip installed
- virtualenv installed

#create virtual environment

- navigate to folder where you want to create your project (e.g. Django_projects)
- create virtual environment
    - virtualenv cocktail_project
- activate virtual environment
    - cd cocktail_project
    - ./scripts/activate.bat
    - ./scripts/activate
 -as a result your virtualenv is activated

#create  a new django project
- install django in your virtual env
    - pip install django
- install pillow library (to upload images)
    - python -m pip install Pillow
- create a Django project
    - django-admin startproject cocktail_app
- open folder cocktail_app in pycharm
- share project on github

#create a new app wihtin your django project
- add app to django projects
    - python manage.py startapp recipes
- add newly added app to INSTALLED APPS (setting.py file)

# update you model
- create recipes class in models.py file
- execute  the migrations
    - python manage.py makemigrations
    - python manage.py migrate


# start server
- python manage.py runserver


