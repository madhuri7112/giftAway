# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from models import *
from Managers import userManager  


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView



def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    a = {"abc":"24"};

    return  JsonResponse({'foo':'bar'});

def user_list_api(request):

    print request.META
    print request.user
    users = User.objects.all()
    result_users = []
    for user in users: 
        result_users.append({"username": user.username, "email": user.email, "password": user.password})

    return JsonResponse({"users": result_users})
    # users = [{"name" : "person 1", "email": "dhs@gmail.com"},{"name" : "person 2", "email": "dhs@gmail.com"}]

    # return  JsonResponse({"users" : users});

def registry_list_api(request):

    registries = [{"owner_id" : 1, "public" : 1}]

    return JsonResponse({"registries" : registries});


def user_details_api(request):

    
    user_details = userManager.get_user(2)

    users = User.objects.all()

    return JsonResponse({"users": users})





@csrf_exempt
def createtoken_api(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    #user.auth_token.delete()
    token = Token.objects.get_or_create(user=user)
    print token
    return JsonResponse({"token" : token[0].key})

@csrf_exempt
def get_user_from_token(request):
      token = request.POST['token']

      token_object = Token.objects.get(key=token)
      return JsonResponse({"user_id" : token_object.user_id})

@csrf_exempt
def delete_token(request):
    token = request.POST['token']
    token_object = Token.objects.get(key=token)
    user_id = token_object.user_id

    user = User.objects.get(id=id)   
    user.auth_token.delete()

    return JsonResponse({"user_id": user_id, "logout": True})

@csrf_exempt
def add_user_api(request):
    
    print request.POST

    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    # username = "Madhurijjnjlgh"
    # email = "dfs@gmail.com"
    # password = "pswrd"
    user = User.objects.create_user(username, email, password)
    
    return JsonResponse({"user": user.username});      


