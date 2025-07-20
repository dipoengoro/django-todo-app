import json
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def todo_list(request):
    # Membaca data dari file db.json
    with open('db.json', 'r') as f:
        todos = json.load(f)

    return render(request, 'todo/index.html', {'todos': todos})

# FUNGSI BARU UNTUK MENAMBAH TUGAS
def add_todo(request):
    if request.method == 'POST':
        # 1. Baca data lama
        with open('db.json', 'r') as f:
            todos = json.load(f)

        # 2. Ambil data dari form
        new_task_next = request.POST.get('task_name')

        # 3. Buat item to-do baru
        new_id = max(item['id'] for item in todos) + 1 if todos else 1
        new_todo = {
            'id': new_id,
            'task': new_task_next,
            'done': False
        }

        # 4. Tambahkan ke list dan tulis kembali ke file
        todos.append(new_todo)
        with open('db.json', 'w') as f:
            json.dump(todos, f, indent=2)


    # 5. Redirect kembali ke halaman utama
    return redirect(reverse('todo_list'))

def delete_todo(request, todo_id):
    with open('db.json', 'r') as f:
        todos = json.load(f)

        todos_to_keep = [item for item in todos if item['id'] != todo_id]

        with open('db.json', 'w') as f:
            json.dump(todos_to_keep, f, indent=2)

        return redirect(reverse('todo_list'))

def edit_todo(request, todo_id):
    if request.method == 'POST':
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

def toggle_done(request, todo_id):
    if request.method == 'POST':
        with open('db.json', 'r') as f:
            todos = json.load(f)

        for item in todos:
            if item['id'] == todo_id:
                item['done'] = not item['done']
                break
        with open('db.json', 'w') as f:
            json.dump(todos, f, indent=2)

    return redirect(reverse('todo_list'))