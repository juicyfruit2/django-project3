from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    
    return HttpResponse("Hi there, you've landed on the stillApp index page.")


def welcome_view(request):
    
    return render(request, 'hello.html')