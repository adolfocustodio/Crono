from django.db import models
from categories.models import Category

class Post(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    file = models.FileField(upload_to='files', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
