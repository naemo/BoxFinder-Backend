from django.db import models
from django.conf import settings

class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()

class ContainerData(models.Model):
    Harbor = models.CharField(max_length=30)
    Date = models.DateField()
    isKorean = models.BooleanField() # 한국에서 사용하는 컨테이너인지
    Full_10 = models.IntegerField() # 규격이 10인 경우
    Empty_10 = models.IntegerField()
    Full_20 = models.IntegerField()
    Empty_20 = models.IntegerField()
    Full_40 = models.IntegerField()
    Empty_40 = models.IntegerField()
    Full_other = models.IntegerField() # 규격 외 
    Empty_other = models.IntegerField() # 규격 외 
    Volume = models.IntegerField() # 용적톤

class Lead(models.Model): #확인을 위한 fakedata
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
