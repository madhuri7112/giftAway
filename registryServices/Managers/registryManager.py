from .. import models
from django.contrib.auth.models import User

def create_registry(user_id, name, public):

    new_registry = models.Registry(owner_id = User.objects.get(id=user_id), name= name, public = public)
    new_registry.save()

    return  {"id": new_registry.id}

def get_registries(user_id):

    registries = models.Registry.objects.filter(owner_id = user_id)

    for reg in registries:

        result.append({"id": reg.id, "name": reg.name, "public": reg.public})

    return result

def get_registry(user_id, registry_id):

    registry = models.Registry.objects.get(id=registry_id)
    registry_items = models.RegistryItem.objects.filter(registry_id=registry_id)

    result = {}
    result['id'] = registry.id
    result['name'] = registry.name
    result['public'] = registry.public

    items = []

    for registry_item in registry_items:
        item = models.Item.objects.get(id=registry_item.item_id.id)
        items.append({
            "id": item.id, 
            "item_code": item.item_code,
            "item_name": item.item_name,
            "price": item.price,
            "category": item.category,
            "colour": item.colour
            })

    result['items'] = items

    return result


def add_registry_item(user_id, registry_id, item_id):
    

    if not is_user_owner_of_registry(user_id, registry_id):
        return {"status" : "Auth error"}
    
    registry = models.Registry.objects.get(id=registry_id)
    item = models.Item.objects.get(id=item_id)
    new_registry_item = models.RegistryItem(registry_id=registry, item_id = item, assigned_to = None)
    new_registry_item.save()

    return {"id":new_registry_item.id}


def remove_registry_item(user_id, registry_id, item_id):

    if not is_user_owner_of_registry(user_id, registry_id):
        return {"status" : "Auth error"}

    #registry = models.Registry.objects.get(id=registry_id)
    registry_item = models.RegistryItem.objects.filter(registry_id=registry_id, item_id=item_id).delete()

    return {"status": "SUCCESS"}


def assign_item(user_id, registry_item_id):

    registry_item = models.RegistryItem.objects.get(id=registry_item_id)
    registry_item.assigned_to = User.objects.get(id=user_id)
    registry_item.save()

    return {"id": registry_item}

def unassignitem(user_id, registry_item_id):

    registry_item = models.RegistryItem.objects.get(id=registry_item_id)
    registry_item.assigned_to = None
    registry_item.save()

    return {"id": registry_item}


def is_user_owner_of_registry(user_id, registry_id):
    registry = models.Registry.objects.get(id=registry_id)
 
    print registry.owner_id.id
    print user_id
    
    if int(registry.owner_id.id) == int(user_id):
    	print "Fhgdhdg"
    	return True
    else:
    	return False

