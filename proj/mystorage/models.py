from django.db import models
from django.conf import settings

class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()

class UserData(models.Model): #로그인에 맞는 회원 정보
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    remember_me = models.NullBooleanField() # 로그인 여부 확인 변수

class Lead(models.Model): #확인을 위한 fakedata
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
