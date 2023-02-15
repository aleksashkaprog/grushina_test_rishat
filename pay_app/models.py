from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
