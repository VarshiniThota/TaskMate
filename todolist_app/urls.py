from django.urls import path
from todolist_app import views


urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<task_id>/',views.delete_task,name='delete'),
    path('edit/<task_id>/',views.edit_task,name='edit'),
    path('status/<task_id>/',views.status_edit,name='status'),
    
]
