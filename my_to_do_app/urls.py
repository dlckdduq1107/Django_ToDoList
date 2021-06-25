from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('createTodo/', views.createTodo,name='createTodo'),## 생성버튼을 눌렀을때
    path('deleteTodo/', views.doneTodo,name='deleteTodo') ## 삭제버튼을 눌렀을때
]