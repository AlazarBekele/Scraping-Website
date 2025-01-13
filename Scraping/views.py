from django.shortcuts import render, redirect
from .form import Post_Input

# Create your views here.

def body (request):

    return render (request, 'body.html')


def index (request):

    Input = Post_Input (request.POST or None)

    if Input.method == 'POST':
        if Input.is_valid():

            Input.save()
            return redirect ('Main')

    return render (request, 'index.html')