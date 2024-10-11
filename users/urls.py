from django.urls import path
from django.views.decorators.cache import cache_page
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserRetrieveAPIView, UserCreateAPIView, UserDestroyAPIView, UserUpdateAPIView, UserListAPIView

app_name = UsersConfig.name
urlpatterns = [
    path('', UserCreateAPIView.as_view(), name='user_create'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('view/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_view'),
    path('list/', cache_page(60)(UserListAPIView.as_view()), name='user_list'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
