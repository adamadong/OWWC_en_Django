from django.shortcuts import render,get_object_or_404, redirect
#from django.http import HttpResponseRedirect
from .models import Team, Equipment
from .forms import MoveForm,SelectForm

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
    return p_s_mapping.get(place,'')

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    place = team.place
    state = team.state
    message = request.session.pop('change_message', '')
    form=MoveForm()
    #print(request.method)
    #print(request.method=='POST')
    old_place = get_object_or_404(Equipment,Id_equipment=team.place.Id_equipment)
    request.session['op']=old_place.Id_equipment
    #print(old_place)
    if request.method == "POST":
        #old_place = get_object_or_404(Equipment,Id_equipment=team.place.Id_equipment)
        #old_state = get_object_or_404(Team,state=team.state)
        #print(old_place)
        #print(old_state)
        form=MoveForm(request.POST,instance=team)
        if form.is_valid():
            #form.save(commit=False)
            #form = MoveForm()
            #old_place = get_object_or_404(Equipment,Id_equipment=team.place.Id_equipment)
            print(old_place)
            print(0)
            old_place.save()
            form=MoveForm(request.POST,instance=team)
            form.save(commit=False)
            new_place = get_object_or_404(Equipment,Id_equipment=team.place.Id_equipment)
            print(new_place)
            print(1)
            new_place.save()
            print(old_place.availability)
            #print(place_to_state(new_place.Id_equipment))
            if (old_place.availability):
                if (new_place.availability):
                    new_place.save()
                    form.save()
                    state = place_to_state(new_place.Id_equipment)
                    team.state=state
                    team.save()
                    #message = 'Place changes successfully' 
                    #request.session['change_message'] = message
                    
                else:
                    form.save(commit=False)
                return redirect('team_detail',pk=pk)
                #print(state)
                #print(message)
                #print(1)
            else:
                request.session['placetogo'] = new_place.Id_equipment
                new_place.save()
                form.save()
                state = place_to_state(new_place.Id_equipment)
                team.state=state
                team.save()
                #message = 'Need another team to complete this place'
                #request.session['change_message'] = message
                return redirect('select_page',pk=pk)
                #message = 'Sry, the place is not availabe now'
                #print(0)
                #print(message)
            #request.session['change_message'] = message
            #return redirect('team_detail',pk=pk)
            #return HttpResponseRedirect(request.path_info + f'?message={message}')
        else:
            form=MoveForm()
            #message='Sry, the form is not valid!'
    #print(state)
    #print(message)
    #message = request.session.pop('change_message', '')
    return render(request,
                  'blog/team_detail.html',
                  {'team': team, 'place': place, 'form': form,'state':state,'message': message})

def select_page(request,pk):
    # 从数据库中获取队伍列表
    sform=SelectForm()
    #oldteam = get_object_or_404(Team, pk=pk)
    #new_place = oldteam.place
    #Oteam = get_object_or_404(Team, pk=pk)
    #old_place = get_object_or_404(Equipment,Id_equipment=Oteam.place.Id_equipment)
    old_place_id = request.session.get('op')
    old_place = get_object_or_404(Equipment,Id_equipment=old_place_id)
    #new_place_id = request.session.get('placetogo')
    #new_place = get_object_or_404(Equipment,Id_equipment=new_place_id)
    #state = Oteam.state
    #print(new_place)
    #print(2)
    #Oteam.place=new_place
    #state = place_to_state(new_place.Id_equipment)
    #Oteam.state=state
    #Oteam.save()
    #print(Oteam.place)
    #print(Oteam.state)
    #print(3)
    #teams = Team.objects.order_by('Country') # 获取所有队伍，你可以根据需要筛选和排序
    #team = get_object_or_404(Team, pk=request.POST.get('Country'))
    #rank = request.POST.get('rank')
    #print(rank)
    #place = team.place
    #state = team.state  
    
    #form=MoveForm()
    if request.method=="POST":
        team = get_object_or_404(Team, pk=request.POST.get('Country'))
        place = team.place
        state = team.state 
        rank =team.rank

        #print(team)
        #old_place = get_object_or_404(Equipment,Id_equipment=team.place.Id_equipment)
        #old_place.save()
        N_new_place = old_place
        print(N_new_place)
        print(4)
        N_new_place.save()

        form = SelectForm(request.POST, instance=team)
        if form.is_valid():
            team.rank=rank
            form.save()
            place=N_new_place
            team.place=place
            state = place_to_state(place.Id_equipment)
            team.state=state
            team.save()
            return redirect('team_detail',pk=pk)
            
        else:
            print(form.errors)
            print(1)
    
    return render(request, 'blog/select_team.html', {'sform':sform})
# Create your views here.
