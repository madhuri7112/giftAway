# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.



def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    a = {"abc":"24"};

    return  JsonResponse({'foo':'bar'});

def user_list(request):

	users = [{"name" : "person 1", "email": "dhs@gmail.com"},{"name" : "person 2", "email": "dhs@gmail.com"}]

	return  JsonResponse({"users" : users});

def registry_list(request):

	registries = [{"owner_id" : 1, "public" : 1}]

	return JsonResponse({"registries" : registries});