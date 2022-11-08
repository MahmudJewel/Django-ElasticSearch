from django.urls import path, include
from .views import home, generate_random_data, PublisherDocumentView


urlpatterns = [
    path('', home, name='home'),
    path('generate', generate_random_data, name='generate'),
    path('search/', PublisherDocumentView.as_view({'get': 'list'}), name='search'),
]
