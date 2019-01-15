# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class alcohol(models.Model):
    t = models.DecimalField(max_digits=9, decimal_places=0)
    v1 = models.DecimalField(max_digits=5, decimal_places=1)
    v2 = models.DecimalField(max_digits=5, decimal_places=1)
    v3 = models.DecimalField(max_digits=5, decimal_places=1)
    v4 = models.DecimalField(max_digits=5, decimal_places=1)
    v5 = models.DecimalField(max_digits=5, decimal_places=1)
