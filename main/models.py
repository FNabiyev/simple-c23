from django.db import models


class Hodimlar(models.Model):
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    mutaxasislik = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.fio

