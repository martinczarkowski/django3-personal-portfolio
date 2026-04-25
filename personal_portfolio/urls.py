"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from generator import views as generator_views
from todo import views as toto_views
from portfolio import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # blog
    path('blog/', include('blog.urls')),
    
    # password generator
    path('generator/', generator_views.generator, name='generator'),
    path('password/', generator_views.password, name='password'),
    
    # contact
    path('contact/', views.contact, name='contact'),

    # auth
    path('signup/', toto_views.signupuser, name='signupuser'),
    path('login/', toto_views.loginuser, name='loginuser'),
    path('logout/', toto_views.logoutuser, name='logoutuser'),

    # todo
    path('todolist', toto_views.todolist, name='todolist'),
    path('create/', toto_views.createtodo, name='createtodo'),
    path('current/', toto_views.currenttodos, name='currenttodos'),
    path('completed/', toto_views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>', toto_views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', toto_views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', toto_views.deletetodo, name='deletetodo'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)