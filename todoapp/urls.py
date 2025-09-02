from django.urls import path
from . import views

urlpatterns=[
    #Add Task
    path('addTask/', views.addTask, name='addTask'),
    #Mark as Completed
    path('completed/<int:pk>/', views.completed, name='completed'),
    #Mark as not Completed
    path('undone/<int:pk>/', views.undone, name='undone'),
    #Delete 
    path('delete/<int:pk>/',views.delete, name='delete'),
    #Edit
    path('edit/<int:pk>/',views.edit, name='edit'),
]