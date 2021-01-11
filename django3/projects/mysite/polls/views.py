from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Poll Apps!!<br>Index Page</h1>')