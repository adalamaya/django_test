from django.http import HttpResponse

def index_adal(request):
    return HttpResponse("Hola bb!!!!!!!!!")

def user(request, user):
    return_user = f"Hola {user}"
    return HttpResponse(return_user)

# Create your views here.
