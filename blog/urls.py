from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_list, name='team_list'),
    path('team/<str:pk>/', views.team_detail, name='team_detail'),
    path('select/<str:pk>/', views.select_page, name='select_page'),
    #path('team/<str:pk>/?<str:message>', views.team_detail, name='team_detail_mes'),
]