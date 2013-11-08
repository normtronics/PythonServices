# Create your views here.
from django.http import HttpResponse
from BlueServices.Login.login import loginEntity

def index(request):
    return HttpResponse("It work people")

def login(request):

    userName = request.GET.get('user')
    password = request.GET.get('password')

    log = loginEntity(userName, password)
    user = log.checkIfInSystem

    if user != 0 :
        return HttpResponse(user)
    else :
        return HttpResponse('Son dont exsist')
