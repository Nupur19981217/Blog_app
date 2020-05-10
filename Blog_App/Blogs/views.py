from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Blog

def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('home/create.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Add(request):
    bg = Blog(title = request.POST['title'], desc = request.POST['desc'], date = request.POST['date'], author = request.POST['author'])
    title = request.POST['title'].replace(" ", "_")
    fname = "../Blog_Files/" + title + ".txt"
    with open(fname, "w") as f:
        f.write(request.POST['blog'])
    bg.save()
    return redirect('http://127.0.0.1:8000/')

def blogs(request):
    bg = Blog.objects.all()
    context = {
        "blogs" : bg,
    }
    template = loader.get_template('home/blogs.html')
    return HttpResponse(template.render(context, request))

def detail(request, title):
    title = title.replace(' ', '_')
    fname = "../Blog_Files/" + title + ".txt"
    data = []
    with open(fname, "r") as f:
        data = f.readlines()

    txt = "\n".join(data)
    return HttpResponse(txt)