from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import BloggerModel


# Create your views here.

# INJECTS FILTERED OBJECT INTO myblogs.html
@login_required
def myblogs(request):
    blog_list = BloggerModel.objects.filter(username=request.user)
    context = {'blog_list': blog_list}

    return render(request, 'authCWapp/myblogs.html', context)
