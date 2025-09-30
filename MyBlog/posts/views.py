from django.shortcuts import render
from .models import Post 

def post_list(request):
    posts_list = Post.objects.all().order_by('-created_at') 
    context = {'posts': posts_list,}
    return render(request, 'posts/post_list.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}
    return render(request, 'posts/post_detail.html', context)