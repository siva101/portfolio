from django.shortcuts import render,get_object_or_404
from .models import Blog

def blog(request):
    blogs=Blog.objects
    return render(request,'blog/blog.html',{'blogs':blogs})

def details(request,blog_id):
    blogdetail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blogdetail})

# Create your views here.
