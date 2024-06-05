from django.db import models
from django.urls import reverse


class Tender(models.Model):

    title = models.CharField(
        max_length=255, verbose_name='Назва тендера'
    )

    description = models.TextField(max_length=200, verbose_name='Опис')

    start_date = models.DateField(verbose_name='Дата початку тендера')

    end_date = models.DateField(verbose_name='Дата закінчення тендера')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'Тендер - {self.title }'

    def get_absolute_url(self):
        return reverse('tender', args=[str(self.id)])


class TenderItem(models.Model):

    name = models.CharField(
        max_length=100, verbose_name='Назва елемента тендера'
    )

    description = models.TextField(max_length=200, verbose_name='Опис')

    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Кількість'
    )

    unit = models.CharField(max_length=50, verbose_name='Одиниця')

    tender = models.ForeignKey(
        Tender, on_delete=models.CASCADE, verbose_name='Тендер', related_name='items'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Елемент тендера - {self.name}'


class Bidder(models.Model):

    name = models.CharField(max_length=255, verbose_name='ПІБ')

    contact_info = models.CharField(max_length=255, verbose_name='Номер телефону')

    def __str__(self):
        return self.name


class Bid(models.Model):

    tender = models.ForeignKey(
        Tender, on_delete=models.CASCADE, verbose_name='Тендер', related_name='bids'
    )

    bidder = models.ForeignKey(
        Bidder, on_delete=models.CASCADE, verbose_name='Учасник', related_name='bids'
    )

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')

    terms = models.TextField(verbose_name='Умови')

    submission_date = models.DateField(auto_now_add=True, verbose_name='Дата подання')

    def __str__(self):
        return f"Пропозиця від - {self.bidder.name} для {self.tender.title}"


class Award(models.Model):

    tender = models.ForeignKey(
        Tender, on_delete=models.CASCADE, verbose_name='Тендер', related_name='awards'
    )

    bidder = models.ForeignKey(
        Bidder, on_delete=models.CASCADE, verbose_name='Учасник', related_name='awards'
    )

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Нагорода')

    terms = models.TextField(verbose_name='Умови')

    award_date = models.DateField(auto_now_add=True, verbose_name='Дата нагородження')

    def __str__(self):
        return f"Нагорода для {self.bidder.name} з {self.tender.title}"



