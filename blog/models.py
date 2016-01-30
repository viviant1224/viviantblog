#encoding:UTF-8
from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()


#add model 20160130 begin
class UserInfo(models.Model):
	nickname = models.CharField(max_length=20)
	work = models.CharField(max_length=20)
	company = models.CharField(max_length=50)
	email = models.CharField(max_length=20)

class BolgBody(models.Model):
	blog_title = models.CharField(max_length=50)
	blog_body = models.TextField()
	blog_type = models.CharField(max_length=50)
	blog_timestamp = models.DateTimeField()
	blog_imgurl = models.CharField(max_length=50, null=True)
	blog_author = models.CharField(max_length=20)

admin.site.register(BlogPost)
admin.site.register(UserInfo)
admin.site.register(BolgBody)
#add model 20160130 end