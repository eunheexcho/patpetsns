from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostForm, CommentForm

@login_required
def profile(request):
    return render(request, 'my_profile/layout.html')

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.tag_save()
            post.save()

            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'my_profile/post_form.html', {
        'form': form,
        })


def comment_new(request):
    pk = request.POST.get('pk')
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form_c = CommentForm(request.POST)
        if form_c.is_valid():
            comment = form_c.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return render(request, 'my_profile/comment_new_ajax.html', {
                'comment': comment,
            })

    else:
        form_c = CommentForm()
    return render(request, 'home/layout.html', {
        'form_c': form_c,
    })