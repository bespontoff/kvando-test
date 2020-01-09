from django.db import models
from django.core import validators

# Create your models here.


class Entry(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    phone = models.CharField(max_length=17,
                             validators=[validators.RegexValidator(regex=r'^\+?1?\d{9,15}$', message="phone invalid")],
                             unique=True,
                             verbose_name='Телефон')
    name = models.CharField(max_length=100,
                            validators=[validators.RegexValidator(regex=r'^[а-яА-ЯёЁa-zA-Z0-9-_\s]+$', message="name invalid")],
                            verbose_name='Имя')

    def __str__(self):
        return self.name
