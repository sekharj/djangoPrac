from django.http import HttpResponse

def home(request):
    return HttpResponse('you are at home page')