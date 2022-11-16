
from django.urls import path
import task.views as views

urlpatterns = [
    path('create_task/', views.createtask.as_view(), name='get-users-list'),
    path('update_task/<int:pk>/', views.UpdateTaskAPI.as_view(), name='update-task'),
    path('delete_task/<int:pk>/', views.DeleteTaskAPI.as_view(), name='delete-task'),
    path('upload_task/', views.uploadtaskbulk.as_view(), name='upload-task'),
]
