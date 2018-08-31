
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact),
    path('Snippet', views.Snippet_detail ),
    
]
