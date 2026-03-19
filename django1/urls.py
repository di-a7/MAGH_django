from django.urls import path
from .views import *
urlpatterns = [
   path('task/', todolist),
   path('task/create/', create)
]
