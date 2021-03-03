from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm


def main_feed(request):
    allPosts = Post.objects.filter(is_published=True).order_by('-publishing_time')
    allRelComments = Comment.objects.filter(is_published=True).order_by('-publishing_time')
    return render(request,
                  "feed/main_feed.html",
                  {'allPosts': allPosts, 'allRelComments': allRelComments})

@login_required()
def edit_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=id)
        if request.method == 'GET':
            form = PostForm(instance=post)
            return render(request,
                          "feed/edit_post_form.html",
                          {'form': form, 'post': post})
        elif request.method == 'POST':
            form = PostForm(instance=post, data=request.POST)
            if form.is_valid():
                form.save()
                post2 = get_object_or_404(Post, pk=post.id)
                post2.photo=request.FILES['photo']
                post2.save()
                return redirect('main_feed')



    else:
        return redirect('publisher_login')


@login_required
def delete_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return redirect('main_feed')
    else:
        return redirect('publisher_login')




@login_required
def new_post(request):
    if request.user.is_authenticated:
        posts = Post.objects.order_by('-id')
        new_id = posts[0].id + 1
        post = Post.objects.create(is_published=True, pk=new_id, author=request.user)
        form = PostForm(instance=post, data=request.GET)
        return render(request,
                      "feed/new_post_form.html",
                      {'form': form, 'post': post})
    else:
        return redirect('publisher_login')

@login_required
def add_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=id)
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            post=get_object_or_404(Post, pk=id)
            post.photo = request.FILES['photo']
            post.save()
            return redirect('main_feed')
    else:
        return redirect('publisher_login')

@login_required
def new_comment(request, post_id):
    if request.user.is_authenticated:
        user = request.user
        comments = Comment.objects.order_by('-id')
        new_id = comments[0].id + 1
        com = Comment.objects.create(is_published=True, pk=new_id, author=user, post=get_object_or_404(Post, pk=post_id))
        form = CommentForm(instance=com, data=request.GET)
        return render(request,
                      "feed/new_comment_form.html", {
                'form': form, 'comment': com
                      })
    else:
        return redirect('publisher_login')

@login_required
def add_comment(request, comment_id):
    if request.user.is_authenticated:
        com = get_object_or_404(Comment, pk=comment_id)
        form = CommentForm(instance=com, data=request.POST)
        if form.is_valid():
            form.save()
            com = get_object_or_404(Comment, pk=comment_id)
            com.photo = request.FILES['photo']
            com.save()
            return redirect('main_feed')
    else:
        return redirect('publisher_login')

@login_required
def delete_comment(request, comment_id):
    if request.user.is_authenticated:
        com = get_object_or_404(Comment, pk=comment_id)
        com.delete()
        return redirect('main_feed')
    else:
        return redirect('publisher_login')

@login_required
def edit_comment(request, comment_id):
    if request.user.is_authenticated:
        com = get_object_or_404(Comment, pk=comment_id)
        if request.method == 'GET':
            form = CommentForm(instance=com)
            return render(request,
                          "feed/edit_comment_form.html",
                          {'form': form, 'comment': com})
        elif request.method == 'POST':
            form = CommentForm(instance=com, data=request.POST)
            if form.is_valid():
                form.save()
                com2 = get_object_or_404(Comment, pk=com.id)
                com2.photo=request.FILES['photo']
                com2.save()
                return redirect('main_feed')
    else:
        return redirect('publisher_login')