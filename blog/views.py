from django.shortcuts import render,get_object_or_404, redirect
from .models import Team, Equipment
from .forms import MoveForm

def show_list(request):
    teams = Team.objects.order_by('rank')
    equipments = Equipment.objects.order_by('Id_equipment')
    context = {'teams': teams, 'equipments': equipments}
    return render(request,'blog/show_list.html',context)

def place_to_state(place):
    p_s_mapping={
        'Restaurant':'Eating',
        'Gymnasium':'Exercising',
        'Hotel':'Resting',
        'Stage':'Playing',
        'Training Room':'Training'
    }

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    place = team.place
    form=MoveForm()
    print(request.method)
    print(request.method=='POST')
    old_place = get_object_or_404(Equipment,Id_equipment=team.place.Id_equipment)
    print(old_place)
    if request.method == "POST":
        old_place = get_object_or_404(Equipment,Id_equipment=team.place.Id_equipment)
        print(old_place)
        form=MoveForm(request.POST,instance=team)
        if form.is_valid():
            old_place = get_object_or_404(Equipment,Id_equipment=team.place.Id_equipment)
            print(old_place)
            old_place.save()
            form.save()
            new_place = get_object_or_404(Equipment,Id_equipment=team.place.Id_equipment)
            print(new_place)
            new_place.save()
            return redirect('team_detail',pk=pk)
        else:
            form=MoveForm()
    
    return render(request,
                  'blog/team_detail.html',
                  {'team': team, 'place': place, 'form': form})

# Create your views here.
