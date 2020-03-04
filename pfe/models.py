# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Role(models.Model):
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)