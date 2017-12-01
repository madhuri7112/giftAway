# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import *
from .Managers import userManager
from .Managers import registryManager
from .Managers import itemManager


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

def index(request):
    a = {"abc":"24"};

    return  JsonResponse({'foo':'bar'});

def user_list_api(request):   
    users = userManager.get_all_users()

    return JsonResponse({"users": users});
   
def user_details_api(request):    
    user_id = request.GET['user_id']
    user_details = userManager.get_user(user_id)
   
    return JsonResponse(user_details)

@csrf_exempt
def createtoken_api(request):

    parameters = json.loads(request.body)
    #parameters = json.loads(request.body
    username = parameters['username']
    password = parameters['password']
    result = userManager.create_token(username, password)

    return JsonResponse(result)

@csrf_exempt
def get_user_from_token_api(request):

    
    token = request.GET['token']
    user_details = userManager.get_user_from_token(token)
     
    return JsonResponse(user_details)

@csrf_exempt
def delete_token_api(request):
    
    parameters = json.loads(request.body)
    token = parameters['token']
    user_id = userManager.delete_token(token)

    return JsonResponse({"user_id": user_id, "logout": True})

@csrf_exempt
def logout_api(request):

     parameters = json.loads(request.body)
     user_id = parameters['user_id']
     result = userManager.logout(user_id)

     return JsonResponse(result)

@csrf_exempt
def register_user_api(request):   
    #print parameters

    parameters = json.loads(request.body)
    username = parameters['username']
    email = parameters['email']
    password = parameters['password']

    result = userManager.register_user(username, email, password)   
     
    return JsonResponse(result);

@csrf_exempt
def change_password_api(request):

    parameters = json.loads(request.body)
    password = parameters['password']
    user_id = parameters['user_id']

    result = userManager.change_password(user_id, password)

    return JsonResponse(result)

@csrf_exempt
def add_item_inventory_api(request):

    parameters = json.loads(request.body)
    result = itemManager.add_item(parameters)

    return JsonResponse(result)

@csrf_exempt
def add_item_registry_api(request):

    parameters = json.loads(request.body)
    registry_id = parameters['registry_id']
    item_id = parameters['item_id']
    user_id = parameters['user_id']

    result = registryManager.add_registry_item(user_id, registry_id, item_id)

    return JsonResponse(result)

@csrf_exempt
def remove_item_registry_api(request):

    parameters = json.loads(request.body)
    registry_id = parameters['registry_id']
    item_id = parameters['item_id']
    user_id = parameters['user_id']

    result = registryManager.remove_registry_item(user_id, registry_id, item_id)

    return JsonResponse(result)

@csrf_exempt
def create_registry_api(request):

    parameters = json.loads(request.body)
    user_id = parameters['user_id']
    public = parameters['public']
    name = parameters['name']

    result = registryManager.create_registry(user_id, name, public)

    return JsonResponse(result)

def get_registry_api(request):

    user_id = request.GET['user_id']
    registry_id = request.GET['registry_id']
    result = registryManager.get_registry(registry_id)

    return JsonResponse(result)


def registry_list_api(request):
    print request
    user_id = request.GET['user_id']
    result = registryManager.get_registries(user_id)

    return JsonResponse(result);

@csrf_exempt
def give_access_registry_api(request):

    parameters = json.loads(request.body)
    user_id = parameters['user_id']
    access_to_user_id = parameters['access_to_user_id']
    registry_id = parameters['registry_id']

    result = registryManager.give_access_registry(user_id, registry_id, access_to_user_id)

    return JsonResponse(result)

@csrf_exempt
def deny_access_registry_api(request):

    parameters = json.loads(request.body)
    user_id = parameters['user_id']
    deny_to_user_id = parameters['deny_to_user_id']
    registry_id = parameters['registry_id']

    result = registryManager.deny_access_registry(user_id, registry_id, deny_to_user_id)

    return JsonResponse(result)


