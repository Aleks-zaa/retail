from rest_framework import generics

from users.models import User
from users.permissions import IsActive
from users.serializers import CreateUserSerializer, UserSerializer


# Create your views here.

class UserCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания пользователей. """
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    """ Контроллер для вывода списка пользователей. """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsActive]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для просмотра пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsActive]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsActive]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsActive]
