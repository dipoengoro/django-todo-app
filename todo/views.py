import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class TodoListView(View):
    def get(self, request):
        """Menangani GET request untuk menampilkan semua tugas."""
        with open('db.json', 'r') as f:
            todos = json.load(f)
        return render(request, 'todo/index.html', {'todos': todos})

    def post(self, request):
        """Menangani POST request dari form 'Add'."""
        print("Data POST yang diterima:", request.POST)
        with open('db.json', 'r') as f:
            todos = json.load(f)

        new_task_text = request.POST.get('task_name')
        new_id = max(item['id'] for item in todos) + 1 if todos else 1
        new_todo = {
            'id': new_id,
            'task': new_task_text,
            'done': False
        }

        todos.append(new_todo)
        with open('db.json', 'w') as f:
            json.dump(todos, f, indent=2)

        return redirect(reverse('todo_list'))

class TodoToggleDoneView(View):
    def post(self, request, todo_id):
        with open('db.json', 'r') as f:
            todos = json.load(f)

        for item in todos:
            if item['id'] == todo_id:
                item['done'] = not item['done']
                break

        with open('db.json', 'w') as f:
            json.dump(todos, f, indent=2)

        return redirect(reverse('todo_list'))

class TodoEditView(View):
    def post(self, request, todo_id):
        with open('db.json', 'r') as f:
            todos = json.load(f)

        new_task_text = request.POST.get('task_name')
        for item in todos:
            if item['id'] == todo_id:
                item['task'] = new_task_text
                break

        with open('db.json', 'w') as f:
            json.dump(todos, f, indent=2)

        return redirect(reverse('todo_list'))

class TodoDeleteView(View):
    def post(self, request, todo_id):
        with open('db.json', 'r') as f:
            todos = json.load(f)

        todos_to_keep = [item for item in todos if item['id'] != todo_id]
        with open('db.json', 'w') as f:
            json.dump(todos_to_keep, f, indent=2)

        return redirect(reverse('todo_list'))