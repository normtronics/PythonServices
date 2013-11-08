# Create your views here.
from django.http import HttpResponse



def index(request):
    return HttpResponse("It work people")

def login(request):

    name = request.GET.get('name')
    password = request.GET.get('password')

    log = login(name, password)

    return HttpResponse(log)
