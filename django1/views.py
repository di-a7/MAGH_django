from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist
# Create your views here.
def home(request):
   people = [
      {
         "name":"ram",
         "age":"25",
         "contact":"98546225555"
      },
      {
         "name":"abc",
         "age":"60",
         "contact":"98546225555"
      },
      {
         "name":"ert",
         "age":"50",
         "contact":"98546225555"
      },
      {
         "name":"ffg",
         "age":"30",
         "contact":"98546225555"
      },
      {
         "name":"ffg",
         "age":"30",
         "contact":"98546225555"
      },
      {
         "name":"ffg",
         "age":"30",
         "contact":"98546225555"
      }
   ]
   context = {
      "title": "HOME Page",
      "body":"HOME",
      "PEOPLE": people
   }
   return render(request,'home.html',context)

def aboutus(request):
   return render(request,'aboutus.html')

# create aboutus, contactus
# aboutus render aboutus html page
# contactus render contact html page


def todolist(request):
   todolist = Todolist.objects.all().order_by("-id")
   completed = Todolist.objects.filter(status = True).count()
   incomplete = Todolist.objects.filter(status = False).count()
   
   context = {
      "tasks":todolist,
      "complete":completed,
      "incomplete":incomplete
   }
   return render(request,'list.html',context)