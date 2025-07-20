from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('delete/<int:todo_id>/', views.TodoDeleteView.as_view(), name='delete_todo'),
    path('edit/<int:todo_id>/', views.TodoEditView.as_view(), name='edit_todo'),
    path('toggle/<int:todo_id>/', views.TodoToggleDoneView.as_view(), name='toggle_done'),
]