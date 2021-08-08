from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Users
from . serializers import UsersSerializer
from django.http import JsonResponse
from first_project.utils.response_helper import Ok
from first_project.utils.exception.business_exception import BusinessException

class UsersList(APIView):
    
    def get(self, request):
        users = Users.objects.all().order_by('id')
        serializer = UsersSerializer(users, many=True)
        return Ok(serializer.data)
    
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Ok(serializer.data)
        raise BusinessException('Create a new User unsuccessful!')

class UsersDetail(APIView):
    
    def get(self, request, *args, **kwargs):
            user = get_object_or_404(Users, id=kwargs.get('pk'))
            serializer = UsersSerializer(user)
            return Ok(serializer.data)
    
    def put(self, request, *args, **kwargs):
        user = get_object_or_404(Users, id=kwargs.get('pk'))
        serializer = UsersSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Ok(serializer.data)
        else:
            raise BusinessException('Update User unsuccessful!')

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(Users, id=kwargs.get('pk'))
        user.delete()
        return Ok(None)
