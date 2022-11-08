from django.urls import path, include
from .views import home, generate_random_data


urlpatterns = [
    path('', home, name='home'),
    path('generate', generate_random_data, name='generate'),
]
