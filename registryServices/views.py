# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from models import *
from Managers import userManager
from Managers import registryManager
from Managers import itemManager


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


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
    username = request.POST['username']
    password = request.POST['password']
    token = userManager.create_token(username, password)

    return JsonResponse({"token" : token})

@csrf_exempt
def get_user_from_token_api(request):
    token = request.POST['token']
    user_id = userManager.get_user_from_token(token)
     
    return JsonResponse({"user_id" : user_id})

@csrf_exempt
def delete_token_api(request):
    token = request.POST['token']
    user_id = userManager.delete_token(token)

    return JsonResponse({"user_id": user_id, "logout": True})

@csrf_exempt
def register_user_api(request):   
    #print request.POST
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    username = userManager.register_user(username, email, password)   
     
    return JsonResponse({"user": username});

@csrf_exempt
def add_item_inventory_api(request):

	params = request.POST
	result = itemManager.add_item(params)

	return JsonResponse(result)

@csrf_exempt
def add_item_registry_api(request):

	registry_id = request.POST['registry_id']
	item_id = request.POST['item_id']
	user_id = request.POST['user_id']

	result = registryManager.add_registry_item(user_id, registry_id, item_id)

	return JsonResponse(result)

@csrf_exempt
def remove_item_registry_api(request):

	registry_id = request.POST['registry_id']
	item_id = request.POST['item_id']
	user_id = request.POST['user_id']

	result = registryManager.remove_registry_item(user_id, registry_id, item_id)

	return JsonResponse(result)

@csrf_exempt
def create_registry_api(request):
    user_id = request.POST['user_id']
    public = request.POST['public']
    name = request.POST['name']

    result = registryManager.create_registry(user_id, name, public)

    return JsonResponse(result)

def get_registry_api(request):

	user_id = request.GET['user_id']
	registry_id = request.GET['registry_id']
	result = registryManager.get_registry(user_id, registry_id)

	return JsonResponse(result)

def registry_list_api(request):

    user_id = request.GET['user_id']
    result = registryManager.get_registries(user_id)

    return JsonResponse(result);

@csrf_exempt
def give_access_registry_api(request):

	user_id = request.POST['user_id']
	access_to_user_id = request.POST['access_to_user_id']
	registry_id = request.POST['registry_id']

	result = registryManager.give_access_registry(user_id, registry_id, access_to_user_id)

	return JsonResponse(result)

@csrf_exempt
def deny_access_registry_api(request):

	user_id = request.POST['user_id']
	deny_to_user_id = request.POST['deny_to_user_id']
	registry_id = request.POST['registry_id']

	result = registryManager.deny_access_registry(user_id, registry_id, deny_to_user_id)

	return JsonResponse(result)


