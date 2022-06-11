from django.http import HttpResponse

# Create your views here.
def login(req):
    return HttpResponse("<p>working...</p>")
