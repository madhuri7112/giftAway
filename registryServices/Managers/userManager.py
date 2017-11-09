from .. import models

def add_user():
    new_user = models.User(name="name", email_id="email_id", password="password", role="role")

    new_user.save()

    return  {"user_id": new_user.id}

def get_user(id):
	
	user = models.User.objects.get(id=id)

	return {"id": user.id, "name": user.name, "email_id": user.email_id, "password": user.password, "role": user.role}