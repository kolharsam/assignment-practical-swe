from django.http import HttpResponse


def health(request):
    return HttpResponse("OK", status=200)


def default(req):
    return HttpResponse("Welcome, home!", status=200)
