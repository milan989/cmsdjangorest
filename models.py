from django.db import models
import datetime

class User(models.Model):
    userid = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=10)


class Post(models.Model):
    postid = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    content = models.CharField(max_length=50)
    creation_date = models.DateField(default=datetime.datetime.today)

    def likes_count(self):
        return self.likes.all().count()

class Likes(models.Model):
    likeid = models.IntegerField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

