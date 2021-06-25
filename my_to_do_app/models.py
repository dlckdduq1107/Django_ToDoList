from django.db import models

# Create your models here.
# 데이터 베이스와 관련된 model
# 하나의 모델은 하나의 클래스로 표현됨

class Todo(models.Model):
    content = models.CharField(max_length=255)#데이터 형태가 CharField이고 최대길이가 255
    isDone = models.BooleanField(default=False)


