from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'mysite/home.html')

def about(request):
    return render(request, 'mysite/about.html', {'title': 'About'})

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'mysite/blog.html', context)

def resources(request):
    return render(request, 'mysite/resources.html')