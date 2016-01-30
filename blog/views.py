#encoding:UTF-8
from django.shortcuts import render
from blog.models import BlogPost, UserInfo, BolgBody

# Create your views here.

def index(request):
	blog_list = BlogPost.objects.all()
	userinfo = UserInfo.objects.first()
	blog_body = BolgBody.objects.all()[:6]
	return render(request, 'index.html', {'blog_list' : blog_list, 'userinfo' : userinfo, 'blog_body' : blog_body})
