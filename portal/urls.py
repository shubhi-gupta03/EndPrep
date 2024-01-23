from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='HOME'),
    path('options',views.options,name='options'),
]