from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

class Item(models.Model):
	item_code = models.IntegerField();
	item_name = models.CharField(max_length=200)
	price = models.IntegerField();
	category = models.CharField(max_length=200)
	colour = models.CharField(max_length=200)

class Registry(models.Model):
	owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
	public = models.BooleanField()

class RegistryItem(models.Model):
	registry_id = models.ForeignKey(Registry, on_delete=models.CASCADE)
	item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

class RegistryAccess():
	registry_id = models.ForeignKey(Registry, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
