from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def post_list(request):
    posts_list = Post.objects.all().order_by("-created_at")
    context = {
        "posts": posts_list,
    }
    return render(request, "posts/post_list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by("-created_at")
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            if request.user.is_authenticated:
                new_comment.user = request.user
            new_comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "posts/post_detail.html", context)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
