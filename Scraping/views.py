from django.shortcuts import render, redirect
from .form import Post_Input

# Create your views here.

def body (request):

    return render (request, 'body.html')


def index (request):

    form = Post_Input (request.POST or None, request.FILES)

    if request.method == 'POST':
        if form.is_valid():

            form.save()
            Post_Input ()
            return redirect ('Main')
        
    context = {
        'form' : form
    }

    return render (request, 'index.html', context=context)