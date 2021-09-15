from django.http import HttpResponse
def wish(request):
    message="Good morning django"
    return HttpResponse(message)

# Create your views here.
