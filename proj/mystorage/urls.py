from django.urls import include, path
from rest_framework.routers import DefaultRouter

from mystorage import views

router = DefaultRouter()
router.register('essay', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]
