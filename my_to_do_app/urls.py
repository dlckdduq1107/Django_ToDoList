from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('createTodo/', views.createTodo,name='createTodo'),## 생성버튼을 눌렀을때
    path('deleteTodo/', views.deleteTodo,name='deleteTodo'), ## 삭제버튼을 눌렀을때
    path('doneTodo/', views.doneTodo,name='doneTodo') ## 삭제버튼 눌렸을때 숨기기

]