from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200,null=True)
    #slug field
    slug=models.SlugField(max_length=100,null=True)
    description=models.TextField(null=True)
    created_at=models.DateTimeField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status_choice=(
    ('unpublished','Unpublished'),
    ('published','Published')
    )
    status=models.CharField(max_length=30,choices=status_choice,default='unpublished',null=True)


    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'slug':self.slug})
