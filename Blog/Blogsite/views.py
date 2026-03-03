from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse



from .models import BlogPost
from .forms import ProductForm


# Create your views here.
def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'Blogsite/index.html', {'blog_posts': blog_posts})
def full_blog_post(request):
    blog_post = BlogPost.objects.get(pk=pk)
    return render(request, 'Blogsite/fullPost.html', {'blog_post': blog_post}
