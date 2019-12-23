from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world FROM SERVER %PUSH_SERVER_PUBLIC_IP%!")

