from django.urls import path
from . import views
from home.dash_apps.finished_apps import simplexample

urlpatterns =[
    path('',views.home ,name='home'),
    path('predict.html',views.predict ,name='predict'),
    path('USA.html',views.usa ,name='usa'),
    path('Australia.html',views.australia ,name='australia'),
    path('England.html',views.england ,name='england'),
    path('Mexico.html',views.mexico ,name='mexico'),
    path('Spain.html',views.mexico ,name='spain')

]