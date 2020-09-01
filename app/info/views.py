from rest_framework import viewsets
from rest_framework.response import Response

from info.models import UserInfo
from info.serializers import UserInfoSerializer


class UserInfoListCreateView(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        return UserInfo.objects.all()

    def create(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

