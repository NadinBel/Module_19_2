from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=30, verbose_name='Введите логин')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    age = models.PositiveSmallIntegerField(verbose_name='Введите ваш возраст')
    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=40)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')



