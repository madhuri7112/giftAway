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




def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    a = {"abc":"24"};

    return  JsonResponse({'foo':'bar'});

def user_list_api(request):

    users = [{"name" : "person 1", "email": "dhs@gmail.com"},{"name" : "person 2", "email": "dhs@gmail.com"}]

    return  JsonResponse({"users" : users});

def registry_list_api(request):

    registries = [{"owner_id" : 1, "public" : 1}]

    return JsonResponse({"registries" : registries});

def user_details_api(request):

    user_details = userManager.get_user(2)

    return JsonResponse(user_details);

@csrf_exempt
def add_user_api(request):
    
    print request.POST

    user = userManager.add_user(request.POST)
    return JsonResponse(user);	


