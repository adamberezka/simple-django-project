from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import CommentForm
from news.models import News

from .models import Comment


@login_required(login_url='/login/')
def add_comment(request, id):
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            news = get_object_or_404(News, id=id)
            comment = comment.save(commit=False)
            comment.author = request.user.username
            comment.news = news
            comment.create_time = timezone.now()
            comment.save()
            return redirect('/news/' + str(id))
        else:
            context = {'form': comment}
            return render(request, 'news/addComment.html', context)
    else:
        news = get_object_or_404(News, id=id)
        comment = CommentForm()
        context = {'form': comment, 'news': news}
        return render(request, 'news/addComment.html', context)


@login_required(login_url='/login/')
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    newsId = comment.news.id
    comment.delete()
    return redirect('/news/' + str(newsId))
