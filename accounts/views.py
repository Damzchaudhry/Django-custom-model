from rest_framework import generics
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from rest_framework.response import Response

from . import models
from . import serializers

def signup(request):
	return render(request,"reg.html")


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer







	