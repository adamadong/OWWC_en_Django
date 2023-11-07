from django.shortcuts import render
from .models import Team, Equipment

def show_list(request):
    teams = Team.objects.order_by('rank')
    equipments = Equipment.objects.order_by('Id_equipment')
    context = {'teams': teams, 'equipments': equipments}
    return render(request,'blog/show_list.html',context)

# Create your views here.
