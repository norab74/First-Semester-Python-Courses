from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test


from . import models
from .forms import BlogCommentBox, PostForm
from .models import Post, CommentOnPost

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def singlePostView(request, blog_post_id):
    # Always fetch the post by the URL param
    post = get_object_or_404(Post, pk=blog_post_id)

    if request.method == 'POST':
        form = BlogCommentBox(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # Redirect back to this post (matches urls.py: name='Single Post', parameter 'blog_post_id')
            return redirect('Single Post', blog_post_id=post.pk)
        else:
            # Fall through and render with errors
            comments = post.comments.order_by('-pub_date') # type: ignore[attr-defined] #Type checker get's mad 
            #about this cuz it's referencing something that doesn't exist until runtime
            return render(request, 'singlePostView.html', {
                'post_title': post.post_title,
                'pub_date': post.pub_date,
                'post_contents': post.post_contents,
                'commentBox': form,
                'comments': comments,
                'post': post,
            })

    # GET request: show empty form + comments
    form = BlogCommentBox()
    comments = post.comments.order_by('-pub_date') #type: ignore[attr-defined] #Same as above
    return render(request, 'blog/singlePostView.html', {
        'post_title': post.post_title,
        'pub_date': post.pub_date,
        'post_contents': post.post_contents,
        'commentBox': form,
        'comments': comments,
        'post': post,
    })

        

    
def listPostView(request):
    newest_posts = models.Post.objects.order_by("-pub_date")[:3]
    template = loader.get_template("blog/blogHome.html")
    context = {"newest_posts" : newest_posts}
    return HttpResponse(template.render(context, request))

def aboutTheOwner(request):
    return render(request, 'homepage/aboutMe.html')

def searchTheBlog(request):
    return HttpResponse("Hello World, This placeholder will eventually host a search engine for the site.")


def is_superuser(user):
    return user.is_authenticated and user.is_superuser #superusers only :)

@login_required
@user_passes_test(is_superuser)
def new_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.author = request.user
            post.save()
            # adjust redirect target to your URL names
            return redirect('Single Post', blog_post_id=post.pk)
        # fall through to re-render form with validation errors
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})
    
        