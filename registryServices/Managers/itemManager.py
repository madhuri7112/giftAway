from .. import models


def add_item(params):
 
    item_code = params['item_code']
    item_name = params['item_name']
    price = params['price']
    category = params['category']
    colour = params['colour']

    new_item = models.Item(
        item_code = item_code,
        item_name = item_name,
        price = price,
        category = category,
        colour = colour
        )

    new_item.save()

    return  {"id": new_item.id}

def remove_item(item_id):

    models.Item.objects.get(id=item_id).delete()

    return {"status": "SUCCESS"}

def search():

    return 0