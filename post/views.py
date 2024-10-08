from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

@login_required
def post_create(request) : 
    if request.method=='POST' : 
        form = PostCreateForm(data = request.POST , files=request.FILES)
        if form.is_valid() : 
            new_item=form.save(commit=False)
            new_item.user=request.user 
            new_item.save()

    else :
         form = PostCreateForm(data = request.GET)
    return render(request , 'post/create.html', {'form':form})


def feed(request) : 
    posts = Post.objects.all()
    return render(request , 'post/feed.html' , {'posts':posts})
