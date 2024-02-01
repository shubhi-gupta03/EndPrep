from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='HOME'),
    path('pdfs', views.pdfs, name='pdfs.html'),
]