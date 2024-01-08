from django.db import models
from users.models import User
from categories.models import Category

class Post(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    file = models.FileField(upload_to='files', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')

    def __str__(self):
        return self.title
