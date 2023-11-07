from django.shortcuts import render
from .models import Team, Equipment

def show_list(request):
    teams = Team.objects.order_by('Country')
    equipments = Equipment.objects.order_by('Id_equipment')
    return render(request,'blog/show_list.html',{'teams':teams},{'equipments':equipments})

# Create your views here.
