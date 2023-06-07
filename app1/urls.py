from django.urls import path
from app1.views import *
app_name='siva1'
urlpatterns= [
    path('siva1/',siva1,name='siva1'),
]