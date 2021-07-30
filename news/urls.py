from django.urls import path
from .views import UyView
urlpatterns =[
    path('',UyView.as_view(),name= 'home')
]

