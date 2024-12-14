from django.db import models
from django.urls import reverse
class Post(models.Model):
    title=models.CharField(max_length=200)
    img=models.ImageField(blank=True)
    text =models.TextField()
    number=models.IntegerField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.pk)])
class Post2(models.Model):
    titlelar=models.CharField(max_length=200)
    imglar=models.ImageField()
    textlar =models.TextField()
    numberlar=models.IntegerField()
    def __str__(self):
        return self.titlelar
    def get_absolute_url(self):
        return reverse('abaut_detail',args=[str(self.pk)])