
from django.urls import path
from .views import TodoList, TodoDetail, TodoUpdate

urlpatterns = [
    path('', TodoList.as_view(), name='todo_list'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
    path('<int:pk>/update/', TodoUpdate.as_view(), name='todo_update'),
]