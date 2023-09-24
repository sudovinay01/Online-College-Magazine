from django.db import models

class AdminModel(models.Model):
    username=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)

class AddCollegeNewsModel(models.Model):
    heading=models.CharField(max_length=200)
    enternews=models.TextField()

class ModeratorModel(models.Model):
    category=models.CharField(choices=(('sports','SPORTS'),('nature','NATURE'),('ourcollege','OURCOLLEGE'),('technology','TECHNOLOGY')),max_length=100)
    moderator_name=models.CharField(max_length=100)
    userid=models.IntegerField(primary_key=True )
    password=models.CharField(max_length=100)
    mobile_num=models.IntegerField()
    email_id=models.EmailField(max_length=200)

class ArticleModel(models.Model):
    articleid=models.IntegerField(primary_key=True)
    category=models.CharField(max_length=50,choices=[('sports','SPORTS'),('nature','NATURE'),('ourcollege','OURCOLLEGE'),
                                                          ('technology','TECHNOLOGY')])
    tag=models.CharField(max_length=100)
    article=models.TextField()

class MemberModel(models.Model):
    member_name=models.CharField(max_length=50)
    member_id=models.IntegerField(primary_key=True)
    password=models.CharField(max_length=100)
    mobile_num=models.IntegerField()
    email_id=models.EmailField(max_length=200)
    address=models.TextField()