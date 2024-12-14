from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(blank=True)
    text = models.TextField( )
    number = models.IntegerField()

    def str(self):
        return self.title

    def get_absolute_url(self):
         return reverse('post_detail', args=[str(self.pk)])
class post2(models.Model):
    titlelar = models.CharField(max_length=200)
    imglar = models.ImageField(blank=True)
    textlar = models.TextField( )
    numberlar = models.IntegerField()
    def str(self):
        return self.titlelar

    def get_absolute_url(self):
         return reverse('post_detail', args=[str(self.pk)])