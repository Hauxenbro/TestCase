from django.db import models
from django.urls import reverse


class Cards(models.Model):
    seria = models.CharField(max_length=255)
    number = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField()
    used_date = models.DateTimeField(auto_now = True, blank=True, null=True)
    summa = models.IntegerField(default=0, blank=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id':self.pk})

    def __str__(self):
        return (str(self.seria) + str(self.number))

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

class Status(models.Model):
    option = models.CharField(max_length=255)

    def __str__(self):
        return self.option

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class History(models.Model):
    card_id = models.ForeignKey('Cards', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
