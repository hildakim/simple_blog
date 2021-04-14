from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    allPost = Blog.objects.all()
    return render(request, 'home.html', {'allPost': allPost})

def detail(request, id):
    recipePost = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'recipePost':recipePost})
    