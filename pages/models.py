from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    your_email   = models.EmailField()
    message_body = models.TextField()



    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# Create your models here for post.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField()
    #image = models.ImageField(upload_to ='images/')
    publish = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
