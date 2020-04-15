from django.core.files import images
from django.db import models

# Create your models here.


class FirstPage(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.CharField(max_length=255, blank=False, null=False)


class ImageOfFirstPage(models.Model):
    images = models.ImageField(upload_to='images/')
    ofFirstPage = models.ForeignKey(FirstPage, on_delete=models.CASCADE)


class SecondPage(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    video = models.FileField(upload_to='images/')
    content = models.CharField(max_length=255, blank=False, null=False)
    ofFirstPage = models.ForeignKey(FirstPage, on_delete=models.CASCADE)


class Answer(models.Model):
    content = models.CharField(max_length=255, blank=False, null=False)


class Password(models.Model):
    password = models.CharField(max_length=255, blank=False, null=False)