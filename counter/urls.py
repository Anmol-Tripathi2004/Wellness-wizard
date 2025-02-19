from django.urls import path
from . import views
from .views import ccc
# from .views import calculator
from .views import course1
from .views import course2
from .views import course3

urlpatterns = [
    path('', views.home, name='home'),
    path('ccc/', ccc, name='ccc'),
    path('course1/',course1, name='course1'),
    path('course2/',course2,name='course2'),
    path('course3/',course3,name='course3'),
    # path('calculator/',calculator ,name='calculator'),
]
