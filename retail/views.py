from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.response import Response

from retail.models import Network
from retail.serializers import NetworkSerializer
from users.permissions import IsActive


# Create your views here.

class NetworkRetrieveAPIView(RetrieveAPIView):
    """ Контроллер для просмотра сети """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActive]


class NetworkListAPIView(ListAPIView):
    """ Контроллер для получения списка сетей """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['country',]


class NetworkUpdateAPIView(UpdateAPIView):
    """ Контроллер для редактирования сети """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActive]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if 'debt' in request.data:
            request.data.pop('debt')
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class NetworkDeleteAPIView(DestroyAPIView):
    """ Контроллер для удаления сети """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActive]


class NetworkCreateAPIView(CreateAPIView):
    """ Контроллер для создания сети """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActive]
