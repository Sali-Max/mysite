from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):

    name = models.CharField(max_length=166)
    text = models.TextField()

    status = models.BooleanField(default=True)  # public post filter
    create_date = models.DateField(default=timezone.now)
    read_time = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # post Creator (User) # (user deleted = delete created post)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    
    def __str__(self):
        return self.name    #  return name

    def get_absolute_url(self):
        return reverse("blog:post", args={self.id}) #   return template address and post id 
    

