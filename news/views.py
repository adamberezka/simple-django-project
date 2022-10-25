from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm
from django.utils import timezone


def view_news(request):
    news = News.objects.order_by('-create_time')
    context = {'news': news}
    return render(request, 'news/index.html', context)


@login_required(login_url='/login/')
def add(request):
    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            news = news.save(commit=False)
            news.author = request.user.username
            news.create_time = timezone.now()
            news.last_edit_time = timezone.now()
            news.save()
            return redirect('/news/' + str(news.id))
        else:
            context = {'form': news}
            return render(request, 'news/add.html', context)
    else:
        news = NewsForm()
        context = {'form': news}
        return render(request, 'news/add.html', context)


def get(request, id):
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request, 'news/view.html', context)


@login_required(login_url='/login/')
def edit(request, id):
    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            newsDB = get_object_or_404(News, id=id)
            newsDB.topic = news.cleaned_data['topic']
            newsDB.text = news.cleaned_data['text']
            newsDB.last_edit_time = timezone.now()
            newsDB.save()
            return redirect('/news/' + str(id))
        else:
            context = {'form': news}
            return render(request, 'news/edit.html', context)
    else:
        newsDB = get_object_or_404(News, id=id)
        newsForm = NewsForm(instance=newsDB)
        context = {'form': newsForm}
        return render(request, 'news/edit.html', context)
