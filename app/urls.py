from django.urls import path
from app.views import *
app_name='siva'
urlpatterns= [
    path('siva/',siva,name='siva'),
]