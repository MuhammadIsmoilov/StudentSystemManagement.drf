from .serializer import MyTokenObtainPairSerializer,RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import AnonymUser
from rest_framework import generics


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = AnonymUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer