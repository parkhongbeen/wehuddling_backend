from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserInfo(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='name')
    phone_number = PhoneNumberField(verbose_name='phone_number')
    old_address = models.CharField(max_length=250,
                                   verbose_name='address',
                                   blank=True)
    new_address = models.CharField(max_length=250,
                                   verbose_name='new_address',
                                   blank=True)

    def __str__(self):
        return self.name
