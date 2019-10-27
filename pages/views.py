from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # step 1 - pip install django
    # step 2 - django-admin startproject <project_name> .
    # step 3 - python manage.py startapp <app_name>
    # step 4: integrate app -
    # add <app_name>.apps.<AppConfig> to "INSTALLED_APPS" in <project>.settings file
    # add urls.py file to <app_name> folder
        # from django.urls import path
        # from . import views
        #
        # urlpatterns = [
        #     path('', views.index, name="index")
        # ]
    # add "include" to import from django.urls in <project> urls.py page
    # add path("", include('pages.urls')) to urlpatterns in <project> urls.py page
    # add "from django.http import HttpResponse" and this function taking in "request" as an argument
    # return HttpResponse
    # run "python manage.py runserver" to start app
    # create .gitignore file with the following
        # *.log
        # *.pot
        # *.pyc
        # __pycache__/
        # local_settings.py
        # db.sqlite3
        # db.sqlite3-journal
        # media
        # venv/
        # .idea/
    # create git and commit changes
    # return HttpResponse("<h1>Hello World</h1>")
    # changed static to render
    return render(request, 'pages/index.html')
# templates are set in <project> settings.py TEMPLATES > DIRS list
# add the new route to the urls

def about(request):
    # requires render
    return render(request, 'pages/about.html')