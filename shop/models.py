from django.db import models
from django.utils.text import slugify
from decimal import Decimal 

class Category(models.Model):
    
    name = models.CharField('Название', max_length=100, verbose_name='Категория')
    slug = models.SlugField('Слаг', unique=True, blank=True)
    description = models.TextField('Описание', blank=True)
    is_alive = models.BooleanField('Активна', default=True)
    

    def __str__(self):
        return self.name
    
class Prouct(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    brand = models.CharField(max_length=100, verbose_name='Бренд')
    descripiton = models.TextField(verbose_name='Описание')


    