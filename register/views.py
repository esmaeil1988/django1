from django.shortcuts import render,HttpResponse

# Create your views here.
def register(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("My first django project!")