from django.db import models


class Stock(models.Model):
    ARTEM = 'АРТЁМ'
    USSURIYSK = 'УССУРИЙСК'
    CITY_CHOICE = [
        (ARTEM, 'АРТЁМ'),
        (USSURIYSK, 'УССУРИЙСК'),
    ]
    city = models.CharField(max_length=15, choices=CITY_CHOICE)

    def __str__(self):
        return str(self.city)


class Place(models.Model):
    SHT = 'ШТУК'
    M2 = 'M^2'
    M3 = 'М^3'
    UNIT_CHOICE = [
        (SHT, 'ШТ'),
        (M2, 'М^2'),
        (M3, 'М^3'),
    ]
    place_num = models.CharField(max_length=4)  # номер места
    good_numbers = models.TextField()  # номер товара
    count = models.FloatField()  # количество
    unit = models.CharField(max_length=15)  # единица измерения
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, default='0')

    def __str__(self):
        return str(self.place_num)


class Worker(models.Model):
    STOCK_MANAGER = 'ЗАВ. СКЛ'
    STOREKEEPER = 'КЛАДОВЩИК'
    TITLE_CHOICE = [
        (STOCK_MANAGER, 'ЗАВЕДУЮЩИЙ СКЛАДА'),
        (STOREKEEPER, 'КЛАДОВЩИК'),
    ]
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    full_name = models.TextField(max_length=25)
    job_title = models.CharField(max_length=25, choices=TITLE_CHOICE)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, default='0')

    def __str__(self):
        return str(self.full_name)
