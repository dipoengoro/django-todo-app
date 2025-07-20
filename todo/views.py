from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Task
class TodoListView(View):
    def get(self, request):
        tasks = Task.objects.all().order_by('id')
        return render(request, 'todo/index.html', {'todos': tasks})

    def post(self, request):
        Task.objects.create(title=request.POST['task_name'])
        return redirect(reverse('todo_list'))

class TodoToggleDoneView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.done = not task.done
        task.save()
        return redirect(reverse('todo_list'))

class TodoEditView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.title = request.POST['task_name']
        task.save()
        return redirect(reverse('todo_list'))

class TodoDeleteView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect(reverse('todo_list'))