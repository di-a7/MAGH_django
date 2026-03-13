from django.shortcuts import render
from django.http import HttpResponse
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
      "body":"!!!!",
      "PEOPLE": people
   }
   return render(request,'home.html',context)

def aboutus(request):
   return HttpResponse("ABOUT US PAGE.")

# create aboutus, contactus
# aboutus render aboutus html page
# contactus render contact html page