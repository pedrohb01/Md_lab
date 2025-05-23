from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('research/', views.research, name='research'),
    path('our-team/', views.our_team, name='our_team'),
    path('publications/', views.publications, name='publications'),
    path('awards/', views.awards, name='awards'),
    path('join-us/', views.join_us, name='join_us'),
]
