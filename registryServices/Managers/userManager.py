from .. import models
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# def add_user():
#     new_user = models.User(name="name", email_id="email_id", password="password", role="role")
#     new_user.save()

#     return  {"user_id": new_user.id}


def get_all_users():

    users = User.objects.all()
    result_users = []
    for user in users: 
        result_users.append({"username": user.username, "email": user.email, "password": user.password})

    return result_users

def get_user(id):
      
    user = User.objects.get(id=id)

    return {"id": user.id, "username": user.username, "email": user.email, "password": user.password}

def create_token(username, password):

    user = authenticate(username=username, password=password)
    token_object = Token.objects.get_or_create(user=user)
    token = token_object[0].key
    result = {"user_id": user.id, "token": token}

    return result

def get_user_from_token(token):

    token_object = Token.objects.get(key=token)
    user_id = token_object.user_id

    return user_id

def delete_token(token):

    token_object = Token.objects.get(key=token)
    user_id = token_object.user_id

    user = User.objects.get(id=id)   
    user.auth_token.delete()

    return user_id

def register_user(username, email, password):

      user = User.objects.create_user(username, email, password)

      return user.username


