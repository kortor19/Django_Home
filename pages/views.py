from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from .forms import *
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    post = Post.objects.all() #get all the post from the database
    context = {
        'post' :post
    } #context variable
    template_name = 'post_list.html' #our html file
    return render(request, template_name, context) #return



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    template_name = 'post_detail.html'
    return render(request, template_name, context)


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    template_name = 'new_post.html'
    context ={
        'form':form
    }
    return render(request, template_name, context)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form':form, 'post' :post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect("post_list")
    return render(request, 'delete.html', {})



def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})

def contact(request):
    template = "contact.html"
    
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
        
    else:
        form = ContactForm()
    context = {
        'form':form,
        }

    return render(request, template, context)

def services(request):
    return render(request, "services.html", {})

def portfolios(request):
    return render(request, "portfolios.html", {})

# def blog(request):
#     return render(request, "blog.html", {})