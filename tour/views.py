from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import TourSerializer
from .models import Tour

# Create your views here.
class TourViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]  # 指定更新的方法是用PATCH

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]  # 一定要調用方法不然會發生奇怪的錯誤
        return [IsAdminUser()]

    def get_queryset(self):
        return Tour.objects.all()

    def get_serializer_class(self):
        return TourSerializer

    def get_serializer_context(self):
        return {"request": self.request}
