from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import CommentForm 

def post_list(request):
    posts_list = Post.objects.all().order_by('-created_at') 
    context = {'posts': posts_list,}
    return render(request, 'posts/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    context = {
        'post':post,
        'comments': comments,
        'form': form,
        }
    return render(request, 'posts/post_detail.html', context)