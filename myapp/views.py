from django.shortcuts import render
from bs4 import BeautifulSoup as bs
from requests.compat import quote_plus
from . import models
import requests

BASE_INDEED_URL = "https://be.indeed.com/jobs?q={}&l={}&sort=date"
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    location = request.POST.get('location')
    models.Search.objects.create(search=search,location=location)

    final_url = BASE_INDEED_URL.format(quote_plus(search),location)
    response = requests.get(final_url)

    data = response.text
    soup = bs(data,'html.parser')
    post_tiles = soup.find_all('h2',class_='title')
    print(post_tiles)
    stuff_for_frontend ={
        'search':search,
        'location':location,

    }
    return render(request,'myapp/new_search.html',stuff_for_frontend)