from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='questions', default=1)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete= models.CASCADE,  default=1)

    def __str__(self):
        return self.question
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)  
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)  
    updated_by = models.ForeignKey(User, on_delete= models.CASCADE, default=1)

    def __str__(self):
        return self.option

class Comment(models.Model):
    commenter = models.CharField(max_length=100)
    body = models.TextField()
    post = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete= models.CASCADE, default=1)
    

    def __str__(self):
        return self.body


