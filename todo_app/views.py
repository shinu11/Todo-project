from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView ,DeleteView
from .forms import Todoforms
from . models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'remain'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'



class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name','priority','date']
    def get_success_url(self):
        return reverse_lazy('objdeatil',kwargs={'pk':self.object.id})



class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = '/'



def home(request):
    obj1=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date= request.POST.get('date')
        obj = Task(name=name, priority=priority,date=date)
        obj.save()

    return render(request,'home.html',{'remain':obj1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'data':task})

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})



# def result(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         obj = Task(name=name, priority=priority)
#         obj.save()
#     return render(request,'result.html')

