from django.urls import path
from app2.views import *
app_name='siva2'
urlpatterns= [
    path('siva2/',siva2,name='siva2'),
]