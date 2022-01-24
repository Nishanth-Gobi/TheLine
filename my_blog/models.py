from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=15)
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return str(self.id) + '|' + self.title + ' | ' + str(self.author) + ' | ' + str(self.pub_date)

    def get_absolute_url(self):
        # return reverse('blogpost-detailed', args=(str(self.id)))
        return reverse('home')
