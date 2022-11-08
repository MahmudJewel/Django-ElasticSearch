from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import requests
import json
from .models import DemoElastic

# from .documents import NewsDocument
# from .serializers import 

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)


def home(request):
    return HttpResponse('Home Page!!!!')


def generate_random_data(request):
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-10-08&sortBy=publishedAt&apiKey=827705eea42e455cba8bf4afafc7da90'
    r = requests.get(url)
    payload = json.loads(r.text)
    payload = payload.get('articles')
    count = 1
    # print('==================> ', payload)
    # print('==================> ', payload.get('articles')[0]['content'])
    for data in payload:
        print("Generated data : ======> ", count)
        print("Title : ======> ", data.get('title'))
        print("Content : ======> ", data.get('content'))
        count=count+1
        DemoElastic.objects.create(
            title = data.get('title'),
            content = data.get('content')
        )
    text = 'Total generated data => ' + str(count)
    return HttpResponse(text)
    # return HttpResponseRedirect('/')








