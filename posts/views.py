from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.http import HttpResponseForbidden

def get_posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(owner=request.user)
    else:
        posts = Post.objects.all()
    
    return render(request, "posts/blogposts.html", {'posts': posts})
    
def liked_posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(likes=request.user)
    else:
        posts = Post.objects.all()
    
    return render(request, "accounts/profile.html", {'posts': posts})
    
def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "posts/postdetail.html", {'post': post})

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = BlogPostForm()
        
    return render(request, 'posts/blogpostform.html', {'form': form})
        
        
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not(request.user == post.owner or request.user.is_superuser):
        return HttpResponseForbidden()
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post.pk)        
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'posts/blogpostform.html', {'form': form})