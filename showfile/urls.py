from django.urls import path
from . import views

app_name = 'showfile'

urlpatterns =[
    path('', views.showfile, name='index'),
    path('csv/', views.lihatcsv, name='csv'),
    path('json/', views.lihatjson, name='json'),
    path('xml/', views.lihatxml, name='xml'),
]