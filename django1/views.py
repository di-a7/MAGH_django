from django.shortcuts import render, redirect
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

def create(request):
   if request.method == "POST":
      user_title = request.POST.get('title')
      user_description = request.POST.get('description')
      if user_title == "" or user_description == "":
         context = {
            "error":":Both field required."
         }
         return render(request,'create.html', context)
      Todolist.objects.create(title = user_title, description = user_description)
      return redirect('/task/')
   return render(request,'create.html')


def complete(request,id):
   task = Todolist.objects.get(id = id)
   task.status = True
   task.save()
   return redirect('/task/')

def update(request, id):
   task = Todolist.objects.get(id = id)
   if request.method == 'POST':
      user_title = request.POST.get('title')
      user_description = request.POST.get('description')
      task.title = user_title
      task.description = user_description
      task.save()
      return redirect('/task/')
   context = {
      'task':task
   }
   return render(request,'update.html', context)

# button in html file, url, view, to delete


# Portfolio 

#### User ###
# FullName
# degree
# course
# contact
# linkin_link
# fb_link
# ista_link
# github_link
# summary
# imagege(optional) ImageField

### Skill ###
# name of skills
# skill_img (optional)


### Projects ###
# Project name
# Project image
# project github_repo

# views: 
# homepage: userdetail, userskill (from database)
# project: project details (from database)

# webpage: landing page, projects 