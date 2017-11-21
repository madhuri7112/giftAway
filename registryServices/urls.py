"""giftAway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^gift/$', views.index, name='index'),
    url(r'^getusers', views.user_list_api, name='user_list'),
    url(r'^getuser', views.user_details_api, name='user_list'),
    url(r'^registeruser', views.register_user_api, name='register_user'),
    url(r'^createtoken', views.createtoken_api, name='create_token'),
    url(r'^userfromtoken', views.get_user_from_token_api, name='user_from_token'),

    url(r'^createregistry', views.create_registry_api, name='create_registry_api'),
    url(r'^getregistry', views.get_registry_api, name='get_registry_api'),
    url(r'^additemtoregistry', views.add_item_registry_api, name='add_item_registry_api'),
    url(r'^removeitemfromregistry', views.remove_item_registry_api, name='remove_item_registry_api'),

    url(r'^additemtoinventory', views.add_item_inventory_api, name='add_item_inventory_api'),
    # url(r'^getregistries', views.registry_list, name='registry_list'),    
    # url(r'^addregistry', views.add_registry, name='add_user'),
    # url(r'^admin/', admin.site.urls),
]
