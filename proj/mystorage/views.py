from rest_framework import viewsets
from mystorage.models import Essay, Lead
from mystorage.serializers import EssaySerializer, LeadSerializer
from rest_framework.filters import SearchFilter
from rest_framework import generics

#from rest_framework.settings import api_settings
#from rest_framework_csv import renderers as r
#->csv를 위한 renderers

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
