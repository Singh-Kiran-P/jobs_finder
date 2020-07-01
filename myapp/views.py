from django.shortcuts import render
from . import models
from myapp.scripts.indeed_scraper import Indeed_Scraper

BASE_INDEED_URL = "https://be.indeed.com/jobs?q={}&l={}&sort=date"
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    location = request.POST.get('location')
    models.Search.objects.create(search=search,location=location)

    scraper = Indeed_Scraper(search, location, 1)

    if scraper.results == False:
        return render(request, 'myapp/new_search.html', {'error_not_found':True})


    stuff_for_frontend ={
        'final_postings':scraper.final_postings,
        'error_not_found': False

    }
    return render(request,'myapp/new_search.html',stuff_for_frontend)