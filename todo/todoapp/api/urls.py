from django.urls import path, re_path
from . import views

app_name = 'api'

urlpatterns = [
    path(r'', views.TaskListAPIView.as_view(), name="task-list"),
    path(r'create/', views.TaskCreateAPIView.as_view(), name="task-create"), 
    re_path(r'detail/(?P<id>[0-9]{1,3})/', views.TaskDetailAPIView.as_view(), name="task-detail"), 
    re_path(r'(?P<id>[0-9]{1,3})/delete/', views.TaskDeleteAPIView.as_view(), name="delete-task"),
    re_path(r'(?P<id>[0-9]{1,3})/update/', views.TaskDeleteUpdateAPIView.as_view(), name="update-task"),
]