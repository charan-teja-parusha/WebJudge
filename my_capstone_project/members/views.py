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
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from .models import Member
from django.db.models import Avg, Max, Min
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse

#import statements for sentimental analysis
import nltk
from textblob import TextBlob
from nltk.tokenize import word_tokenize
import spacy
import re

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('allmembers.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='/register/')
def details(request, brandname):
  print("details page")
  mymember = Member.objects.filter(brandname__iexact=brandname)
  mymembersize=0.0
  mymemberagg=mymember.aggregate(Avg("ratings"))
  mymembersize=round(mymemberagg.get('ratings__avg'),1)
  print(Member.objects.filter(ratings__gte=3,brandname__iexact=brandname))
  topratings=Member.objects.filter(brandname__iexact=brandname,ratings__gte=3).order_by('-ratings')[:5].values
  bottomratings=Member.objects.filter(brandname__iexact=brandname,ratings__lte=2).order_by('ratings')[:5].values
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
    'ratings':mymembersize,
    'topreviews':topratings,
    'bottomreviews':bottomratings,
  }
  return HttpResponse(template.render(context, request))

"""
def search_request2(request):
  print("hello")
  bname=request.POST['search_query']
  print(bname)
  mymember = Member.objects.filter(brandname="Motorola")
  print(mymember)
  if mymember.exists():
    mymembersize=round(mymember.aggregate(Avg("ratings")).get('ratings__avg'),1)
    topratings=Member.objects.filter(brandname=bname).order_by('-ratings')[:5].values
    bottomratings=topratings=Member.objects.filter(brandname=bname).order_by('ratings')[:5].values
    template = loader.get_template('details.html')
    context = {
      'mymember': mymember,
      'ratings':mymembersize,
      'topreviews':topratings,
      'bottomreviews':bottomratings,
    }
    return render(request,'members/details.html',context)
  else:
    template = loader.get_template('mainnoresults.html')
    return HttpResponse(template.render())


def search_request(request):
  print("hello")
  bname="Motorola"
  #bname=request.POST['search_query']
  print(bname)
  return redirect('details', brandname=bname)


def search_request_details(request):
  print("hello")
  bname=request.POST['search_query']
  print(bname)
  mymember = Member.objects.filter(brandname="Motorola")
  print(mymember)
  if mymember.exists():
    mymembersize=round(mymember.aggregate(Avg("ratings")).get('ratings__avg'),1)
    topratings=Member.objects.filter(brandname=bname).order_by('-ratings')[:5].values
    bottomratings=topratings=Member.objects.filter(brandname=bname).order_by('ratings')[:5].values
    template = loader.get_template('details.html')
    context = {
      'mymember': mymember,
      'ratings':mymembersize,
      'topreviews':topratings,
      'bottomreviews':bottomratings,
    }
    return render(request,'members/details.html',context)
  else:
    template = loader.get_template('mainnoresults.html')
    return HttpResponse(template.render())
"""
@csrf_protect
def main(request):
  print("hello")
  print("request1",request)
  #print(request.GET['search_query'])
  bname=request.GET.get('search_query',False)
  print("searchq",bname)
  review_input=request.POST.get('review_input',False)
  print(review_input)
  if review_input==False:
    if bname==False:
      template = loader.get_template('home.html')
      return HttpResponse(template.render())
    else:
      print("membername ", bname)
      mymember = Member.objects.filter(brandname__iexact=bname)
      print(mymember)
      if mymember.exists():
        mymembersize=round(mymember.aggregate(Avg("ratings")).get('ratings__avg'),1)
        topratings=Member.objects.filter(brandname__iexact=bname,ratings__gte=2.5).order_by('-ratings')[:5].values
        bottomratings=Member.objects.filter(brandname__iexact=bname,ratings__lt=2.5).order_by('ratings')[:5].values
        
        template = loader.get_template('details.html')
        context = {
          'mymember': mymember,
          'ratings':mymembersize,
          'topreviews':topratings,
          'bottomreviews':bottomratings,
        }
        return HttpResponse(template.render(context, request))
      else:
        template = loader.get_template('mainnoresults.html')
        return HttpResponse(template.render())
  else:
    c={}
    detail_brandname=request.POST.get('detail_brandname',False)
    print("request2",request)
    print("detail_brandname",detail_brandname)
    #detail_brandname="test"
    newmember=Member(productname = "Webjudge ProductName",brandname= detail_brandname,price=0,reviews = review_input,ratings=calculate_ratings(review_input),reviewvotes=0)
    newmember.save()
    mymember = Member.objects.filter(brandname__iexact=detail_brandname)
    if mymember.exists():
      mymembersize=round(mymember.aggregate(Avg("ratings")).get('ratings__avg'),1)
      topratings=Member.objects.filter(brandname__iexact=detail_brandname,ratings__gte=2.5).order_by('-ratings')[:5].values
      bottomratings=Member.objects.filter(brandname__iexact=detail_brandname,ratings__lt=2.5).order_by('ratings')[:5].values
      template = loader.get_template('details.html')
      form={}
      # context = {
      #     'mymember': mymember,
      #     'ratings':mymembersize,
      #     'topreviews':topratings,
      #     'bottomreviews':bottomratings,
      #   }
      # form = {}
      # url = reverse('details', args=[detail_brandname])
      # return HttpResponseRedirect(url)

      template = loader.get_template('details.html')
      context = {
        'mymember': mymember,
        'ratings':mymembersize,
        'topreviews':topratings,
        'bottomreviews':bottomratings,
      }
      return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('mainnoresults.html')
        return HttpResponse(template.render())


#method to calculate rating for new review after sentimental analysis score      
def calculate_ratings(reviews):
  nlp = spacy.load('en_core_web_sm', disable=['ner', 'parser'])
  #  preprocess the text using spaCy
  # Remove non-alphabetic characters and convert to lowercase
  text = re.sub('[^A-Za-z]+', ' ', reviews).lower()

  # Tokenize the text using spaCy
  doc = nlp(text)
  tokens = [token.lemma_ for token in doc if not token.is_stop]

  # Combine the tokens into a string
  review_result=' '.join(tokens)  
  sentimentscore=TextBlob(review_result).sentiment.polarity
  sentimentscore=(sentimentscore+1)*2.5
  print(sentimentscore)
  return sentimentscore


def testing(request):
  temp=loader.get_template('testing.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(temp.render(context,request))

def home(request):
  return render(request, 'home.html')
  
def compare(request):
  return render(request, 'compare.html')

def search(request):
  bname = request.GET.get('q')
  column = request.GET.get('column')
  review_input=request.POST.get('review_input',False)
  print(review_input)
  if review_input==False:
    if bname==False:
      template = loader.get_template('home.html')
      return HttpResponse(template.render())
    else:
      print("membername ", bname)
      mymember = Member.objects.filter(brandname__iexact=bname)
      print(mymember)
      if mymember.exists():
        mymembersize=round(mymember.aggregate(Avg("ratings")).get('ratings__avg'),1)
        topratings=Member.objects.filter(brandname__iexact=bname,ratings__gte=2.5).order_by('-ratings')[:5].values
        bottomratings=Member.objects.filter(brandname__iexact=bname,ratings__lt=2.5).order_by('ratings')[:5].values
        template = loader.get_template('search-result.html')
        context = {
          'mymember': mymember,
          'ratings':mymembersize,
          'topreviews':topratings,
          'bottomreviews':bottomratings,
        }
        return HttpResponse(template.render(context, request))
      else:
        template = loader.get_template('mainnoresults.html')
        return HttpResponse(template.render())
  else:
    c={}
    detail_brandname=request.POST.get('detail_brandname',False)
    print("request2",request)
    print("detail_brandname",detail_brandname)
    #detail_brandname="test"
    newmember=Member(productname = "Webjudge ProductName",brandname= detail_brandname,price=0,reviews = review_input,ratings=calculate_ratings(review_input),reviewvotes=0)
    newmember.save()
    mymember = Member.objects.filter(brandname__iexact=detail_brandname)
    if mymember.exists():
      mymembersize=round(mymember.aggregate(Avg("ratings")).get('ratings__avg'),1)
      topratings=Member.objects.filter(brandname__iexact=detail_brandname,ratings__gte=2.5).order_by('-ratings')[:5].values
      bottomratings=Member.objects.filter(brandname__iexact=detail_brandname,ratings__lt=2.5).order_by('ratings')[:5].values
      template = loader.get_template('search-result.html')
      form={}
      context = {
          'mymember': mymember,
          'ratings':mymembersize,
          'topreviews':topratings,
          'bottomreviews':bottomratings,
        }
      form = {}
      url = reverse('search-result',detail_brandname)
      return HttpResponseRedirect(url)
    else:
      template = loader.get_template('mainnoresults.html')
      return HttpResponse(template.render())
