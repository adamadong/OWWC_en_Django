from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_list, name='team_list'),
    path('team/<str:pk>/', views.team_detail, name='team_detail'),
    #path('team/<str:pk>/?<str:message>', views.team_detail, name='team_detail_mes'),
]