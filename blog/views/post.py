from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import os
from blog.forms import CreatePostForm
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
        'due_date': post.due_date
    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def post_create(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            if not post.due_date:  # Если срок не указан, можно установить значение по умолчанию
                post.due_date = None
            post.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, 'blog/post_create.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post-detail', pk=pk)
    else:
        form = CreatePostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post-list')
