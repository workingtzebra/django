from ninja import NinjaAPI, Schema
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from ninja.security import django_auth
from typing import List

api = NinjaAPI()
User = get_user_model()


class UserSchema(Schema):
    id: int
    username: str
    email: str
    # Add other fields you want to include


api = NinjaAPI()


@api.get("/users", response=List[UserSchema], auth=django_auth)
@login_required
def get_users(request):
    users = User.objects.all()
    return users


@api.get("/hello")
def hello(request):
    return "Hello world"
