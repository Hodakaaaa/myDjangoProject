from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import BlogForm  
from .models import Blog  
from django.db.models import Q
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def home_view(request):
#     return render(request, 'display.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact_views(request):
    return render(request, 'contact.html')

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            subheading = form.cleaned_data['subheading']
            description = form.cleaned_data['description']

            blog = Blog(title=title, subheading=subheading, description=description)
            blog.save()
            return redirect('display')  # Redirect to the display_blog_posts view after successful creation
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})

def display_blog_posts(request):
    blog_posts = Blog.objects.all()
    print('Blog Posts:', blog_posts)
    return render(request, 'display.html', {'blog_posts': blog_posts})


def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('display')  # Redirect to the display_blog_posts view after successful update
    else:
        form = BlogForm(instance=blog)

    return render(request, 'update_blog.html', {'form': form, 'blog': blog})

def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('display')  # Redirect to the display_blog_posts view after successful delete

    return render(request, 'delete_blog.html', {'blog': blog})




def search_results(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(subheading__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        posts = Post.objects.none()  # Return an empty queryset if no search query is provided.

    return render(request, 'search_results.html', {'posts': posts})


def post(request):
    return render(request, 'post.html')






















