from django.shortcuts import render,get_list_or_404,redirect
from .models import Login
from .form import LoginForm


def index(request):
    tabledata = [
        ['user'],
        ['sal'],
        ['num'],
        ['del']
    ]
    loginform = Login.objects.all()
    return render(request, 'index.html', {'tabledata': loginform})


def adduser(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        n = form.cleaned_data['username']
        s = form.cleaned_data['salary']
        num = form.cleaned_data['number']
        print(num)
        form.save()
        return redirect('htmx:index')
    else:
        form = LoginForm()
    return render(request, 'add.html', context)
def delete_event(request,event_id):
    event=Login.objects.get(pk=event_id)
    event.delete()
    loginform = Login.objects.all()
    return render(request,'table.html',{'tabledata': loginform})
def edit_event(request,event_id):
    event=Login.objects.get(pk=event_id)
    if request.method == 'POST':
        form = LoginForm(request.POST,instance=event)
        if form.is_valid():
            new_event = form.save()
            return render(request,'tr.html',{'event':new_event})
    else:
        form = LoginForm(instance=event)
        return render(request,'edit.html',{'form':form,'event':event})
