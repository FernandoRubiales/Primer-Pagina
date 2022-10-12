from django.http import HttpResponse

def hello(request):

    return HttpResponse("Hola, esta es mi primer página.")

def bye(request):
    
    return HttpResponse("Hasta luego.")
    