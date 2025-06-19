from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import RegisterAPIView, LoginAPIView, UserProfileAPIView, LogoutAPIView


urlpatterns = [
    path('api/auth/register/', RegisterAPIView.as_view(), name='register'),
    path('api/auth/login/', LoginAPIView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/user/', UserProfileAPIView.as_view(), name='user-profile'),
    path('api/auth/logout/', LogoutAPIView.as_view(), name='logout'),
    
    path('api/', include('projects.urls')),
]