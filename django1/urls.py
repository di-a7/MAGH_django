from django.urls import path
from .views import todolist
urlpatterns = [
   path('list/', todolist)
]
