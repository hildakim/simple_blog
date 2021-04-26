from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    allPost = Blog.objects.all()
    return render(request, 'home.html', {'allPost': allPost})

def detail(request, id):
    recipePost = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'recipePost':recipePost})
    
def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.food_title = request.POST['title']
    new_blog.nickname = request.POST['writer']
    new_blog.recipe = request.POST['body']
    new_blog.upload_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id = id)
    update_blog.food_title = request.POST['title']
    update_blog.nickname = request.POST['writer']
    update_blog.recipe = request.POST['body']
    update_blog.upload_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)