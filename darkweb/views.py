from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import RegForm, LoginForm, BlogCommentForm
from .models import Blog, Comments



def homepage(request):
    blogs = Blog.objects.all().order_by('-published_date')
    user = request.user if request.user.is_authenticated else None  # Foydalanuvchi ma'lumotini olish
    return render(request, 'home.html', {'blogs': blogs, 'user': user})



def registration(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Ro‘yxatdan o‘tgan foydalanuvchini tizimga kiritish
            return redirect('home')
    else:
        form = RegForm()
    return render(request, 'registration.html', {'form': form})


def sign_in(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')

def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    comments = Comments.objects.filter(blog=blog).order_by('-published_date')

    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.user  # Foydalanuvchini qo‘shamiz
            comment.blog = blog  # Blogni belgilaymiz
            comment.save()
            return redirect('detail', id=blog.id)
    else:
        form = BlogCommentForm()

    return render(request, 'detail.html', {'blog': blog, 'comments': comments, 'form': form})
