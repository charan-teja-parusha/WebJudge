#from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

#def members(request):
#    return HttpResponse("Hello world!")
    
    
#from django.http import HttpResponse
#from django.template import loader

#def members(request):
#  template = loader.get_template('listmember.html')
#  return HttpResponse(template.render())
  
  
  
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.contrib.auth.decorators import login_required

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('allmembers.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='/register/')
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template=loader.get_template('main.html')
  return HttpResponse(template.render())
  
def testing(request):
  temp=loader.get_template('testing.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(temp.render(context,request))