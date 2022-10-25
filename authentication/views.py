from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import LoginForm


def log_in(request):
    if request.user.is_authenticated:
        return redirect('view_news')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                if request.POST.get('next') == '':
                    return redirect('/news')
                else:
                    return redirect(request.POST.get('next'))
            else:
                context = {'form': form}
                return render(request, 'authentication/login.html', context)
        else:
            context = {'form': form}
            return render(request, 'authentication/login.html', context)
    else:
        context = {'form': LoginForm()}
        return render(request, 'authentication/login.html', context)
