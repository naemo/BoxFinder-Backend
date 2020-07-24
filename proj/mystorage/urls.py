from django.urls import include, path
from rest_framework.routers import DefaultRouter

from mystorage import views

router = DefaultRouter()
router.register('lead', views.LeadViewSet)
router.register('essay', views.PostViewSet)
router.register('user', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('logincheck/', views.UserList.as_view()), # html 회원 정보 확인용
    path('login/', views.Login.as_view(), name="login"), # html 회원 정보 확인용
]
