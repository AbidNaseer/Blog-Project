from django.shortcuts import render
from .models import Posts
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_posts(request):
    posts = Posts.objects.all().order_by('created_at')
    return render(request, 'all_posts.html', {'posts': posts})
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('all_posts')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})
@login_required
def update_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id, user= request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance= post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('all_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id, user=request.user)
    
    if request.method == 'POST':
        post.delete()
        return redirect('all_posts')  # ✅ only for POST

    return render(request, 'post_delete.html', {'post': post})  
