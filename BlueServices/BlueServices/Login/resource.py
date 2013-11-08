from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import login

class loginResource(ModelResource):
    class Meta:
        queryset = login.objects.all()
        resource_name = 'login'

