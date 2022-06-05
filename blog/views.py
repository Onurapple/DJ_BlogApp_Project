from contextlib import contextmanager
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm



def post_list(request):
    posts = Post.objects.all()
    
    context = {
        "posts" : posts
    }
    return render(request, "blog/post_list.html", context)


def post_add(request):
    form = PostForm()
    print(request.POST)
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            posta = form.save()
            if 'image' in request.FILES:
                posta.image = request.FILES['image']
                posta.save()
            return redirect("list")
    
    context = {
        "form" : form
    }
    return render(request, "blog/post_add.html", context)


def post_update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("list")
    
    context = {
        "form" : form
    }
    return render(request, "blog/post_update.html", context)


def post_delete(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == "POST":
        post.delete()
        return redirect("list")
    
    context = {
        "post" : post
    }
    
    return render(request, "blog/post_delete.html", context)
    

def post_detail(request, id):        
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }    
    return render(request, 'blog/post_detail.html', context)



