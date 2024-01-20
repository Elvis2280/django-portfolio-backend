from django.http import HttpResponse

# Create your views here.
def Index(request: object):
    return HttpResponse("Hello, world. You're at the dashboard index.")

