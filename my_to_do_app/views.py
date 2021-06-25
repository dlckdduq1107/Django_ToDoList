from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request, "my_to_do_app/index.html", content)

def createTodo(request): # 데이터 생성
    user_input_str = request.POST['todoContent'] # 입력칸의 name을 POST 받는다.
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("execute create =>" +user_input_str)

def doneTodo(request):# 데이터 삭제 함수
    done_todo_id = request.GET['todoNum'] # todoNum이라는 id를 보고 GET받아옴
    print("완료한 todo의 id ", done_todo_id)
    todo = Todo.objects.get(id=done_todo_id) # 데이터베이스에서 해당 id에 해당하는 값 가져옴
    todo.delete() # 데이터 삭제
    return HttpResponseRedirect(reverse('index'))
    
