import json
import uuid
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class TodoManager:
    def __init__(self, filepath='db.json'):
        self.filepath = filepath

    def _read_todos(self):
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _write_todos(self, todos):
        with open(self.filepath, 'w') as f:
            json.dump(todos, f, indent=2)

    def get_all(self):
        all_todos = self._read_todos()
        return [item for item in all_todos if not item.get('is_deleted', False)]

    def add(self, task_name):
        todos = self._read_todos()
        new_id = str(uuid.uuid4())
        new_todo = {
            'id': new_id,
            'task': task_name,
            'done': False,
            'is_deleted': False,
        }
        todos.append(new_todo)
        self._write_todos(todos)

    def toggle(self, todo_id):
        todos = self._read_todos()
        for item in todos:
            if str(item['id']) == str(todo_id):
                item['done'] = not item['done']
                break
        self._write_todos(todos)

    def update(self, todo_id, new_task):
        todos = self._read_todos()
        for item in todos:
            if str(item['id']) == str(todo_id):
                item['task'] = new_task
                break
        self._write_todos(todos)

    def soft_delete(self, todo_id):
        todos = self._read_todos()
        for item in todos:
            if str(item['id']) == str(todo_id):
                item['is_deleted'] = True
                break
        self._write_todos(todos)

todo_manager = TodoManager()
class TodoListView(View):
    def get(self, request):
        todos = todo_manager.get_all()
        return render(request, 'todo/index.html', {'todos': todos})

    def post(self, request):
        todo_manager.add(request.POST.get('task_name'))
        return redirect(reverse('todo_list'))

class TodoToggleDoneView(View):
    def post(self, request, todo_id):
        todo_manager.toggle(todo_id)
        return redirect(reverse('todo_list'))

class TodoEditView(View):
    def post(self, request, todo_id):
        todo_manager.update(todo_id, request.POST.get('task_name'))
        return redirect(reverse('todo_list'))

class TodoDeleteView(View):
    def post(self, request, todo_id):
        todo_manager.soft_delete(todo_id)
        return redirect(reverse('todo_list'))