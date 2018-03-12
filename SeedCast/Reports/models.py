from django.db import models
from datetime import datetime

# Create your models here.
from Masters.models import VAW_Registration, Dealer_Registration, STRVVariety


class VAWDemand(models.Model):
    vaw = models.ForeignKey(VAW_Registration, db_column='VAW_Registration_id')
    village_name = models.CharField(max_length=255)
    variety_name = models.ForeignKey(STRVVariety)
    varietyName = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    date_collected = models.DateField(default=datetime.now())
    check = models.BooleanField()

    class Meta:
        verbose_name = 'VAW-Demand'
        verbose_name_plural = 'VAW-Demands'

    def __str__(self):
        return str(self.village_name)

class DealerDemand(models.Model):
    dealer = models.ForeignKey(Dealer_Registration, db_column='Dealer_Registration_id')
    variety_name = models.ForeignKey(STRVVariety)
    quantity = models.PositiveIntegerField()
    date_collected = models.DateField()
    chk = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Dealer Demand'
        verbose_name_plural = 'Dealer Demands'

    def __str__(self):
        return str(self.quantity)