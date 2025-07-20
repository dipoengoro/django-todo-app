from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete_todo'),
    path('edit/<int:pk>/', views.TodoEditView.as_view(), name='edit_todo'),
    path('toggle/<int:pk>/', views.TodoToggleDoneView.as_view(), name='toggle_done'),
]