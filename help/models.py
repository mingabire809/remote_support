from django.db import models


# Create your models here.

class Help(models.Model):
    full_name = models.CharField(verbose_name='Name', max_length=150)
    email = models.CharField(verbose_name='Email', max_length=150)
    phone = models.BigIntegerField(verbose_name='Phone Number')
    subject = models.CharField(verbose_name='Type of issues', max_length=250)
    description = models.TextField(verbose_name='Issue Description')
    address = models.CharField(verbose_name='Address', max_length=250)

    def __str__(self):
        return f'{self.full_name}, {self.email}, {self.phone}, {self.subject}, {self.description}, {self.address}'
