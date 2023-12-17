# from django.shortcuts import render
# from bs4 import BeautifulSoup
# import requests
# from .models import Links
# from django.http import HttpResponseRedirect
# # Create your views here.
# def home(request):
#      if request.method =='POST':
#           input_link=request.POST.get('page','')
#           urls = requests.get(input_link)
#           beautifulsoup = BeautifulSoup(urls.text, 'html.parser')
#
#      for  link in beautifulsoup.find_all('a'):
#           li_address=link.get('href')
#           li_name=link.string
#           Links.objects.create(address=li_address,stringname=li_name)
#           return HttpResponseRedirect('/')
#      else:
#           data_values=Links.objects.all()
#      return render(request, 'home.html',{'data_values':data_values})
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import Links
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        input_link = request.POST.get('page', '')
        urls = requests.get(input_link)
        beautifulsoup = BeautifulSoup(urls.text, 'html.parser')

        for link in beautifulsoup.find_all('a'):
            li_address = link.get('href')
            li_name = link.string
            Links.objects.create(address=li_address, stringname=li_name)

        return HttpResponseRedirect('/')

    else:
        data_values = Links.objects.all()

    return render(request, 'home.html', {'data_values': data_values})
