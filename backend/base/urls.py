from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import * 
from django.urls import path,include

router = DefaultRouter()

router.register('register', RegisterViewset, basename='register')
router.register('users', UserViewset, basename='users')
router.register("logout", LogoutViewSet, basename="logout")
urlpatterns = [
     path('', include(router.urls)),
    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
]