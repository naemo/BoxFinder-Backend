from rest_framework import viewsets
from mystorage.models import Essay, Lead, UserData
from mystorage.serializers import EssaySerializer, LeadSerializer, LoginSerializer
from rest_framework.filters import SearchFilter
from rest_framework import generics

#from rest_framework.settings import api_settings
#from rest_framework_csv import renderers as r
#->csv를 위한 renderers

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.template.loader import render_to_string
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    search_fields = ('name', 'email', 'message')

    def perform_create(self, serializer):
        serializer.save()
    # fake data

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else:
            qs = qs.none()
        return qs

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = LoginSerializer
    search_fields = ('pk','email', 'password', 'remember_me')
    def perform_create(self, serializer):
        serializer.save()
    # 회원 데이터 확인용(api)

class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
        queryset = UserData.objects.all()
        return Response({'profiles': queryset})
    # 회원 정보가 html에 뜨는지 확인용

class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Login.html'
    serializer_class = LoginSerializer
    # 로그인 화면