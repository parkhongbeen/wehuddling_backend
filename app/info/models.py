from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserInfo(models.Model):
    phone_number = PhoneNumberField(verbose_name='phone_number')
    address = models.CharField(max_length=250, verbose_name='address', blank=True)
    new_address = models.CharField(max_length=250, verbose_name='new_address', blank=True)

    def __str__(self):
        return f'전화번호:{self.phone_number}, 구주소:{self.address}, 신주소:{self.new_address}'
