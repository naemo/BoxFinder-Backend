from django.urls import include, path
from rest_framework.routers import DefaultRouter

from mystorage import views

router = DefaultRouter()
router.register('lead', views.LeadViewSet) # fake data  
router.register('essay', views.PostViewSet) # 글쓰기 관련 데이터    
router.register('user', views.UserViewSet) # 

urlpatterns = [
    path('api/', include(router.urls)), # api 확인용!
    path('', views.UserList.as_view()), # html 회원 정보 확인용
    path('rest-auth/', include('rest_auth.urls')), 
    path('rest-auth/registration', include('rest_auth.registration.urls')),
]

REST_USE_JWT=True