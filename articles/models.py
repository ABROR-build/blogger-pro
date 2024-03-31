from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.pk)])