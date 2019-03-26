from django.db import models


# Create your models here.
class idconfig(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    config = models.CharField(max_length=1000)
    capturedserver = models.CharField(max_length=200)
    interval = models.CharField(max_length=200)


class rtsp(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    res_name = models.CharField(max_length=200)
    camid = models.CharField(max_length=200)
    rtsp = models.CharField(max_length=1000)
    cam_name = models.CharField(max_length=200)
