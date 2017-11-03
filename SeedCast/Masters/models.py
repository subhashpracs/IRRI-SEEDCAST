from datetime import datetime

from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext_lazy as _
from django import forms


# Create your models here.
class States(models.Model):
    state_name = models.CharField(max_length=100, primary_key=True)
    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')

    def __str__(self):
        return self.state_name


class Districts(models.Model):
    state_name = models.ForeignKey(States)
    dist_name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        verbose_name = _('District')
        verbose_name_plural = _('District\'s')

    def __str__(self):
        return self.dist_name

class Blocks(models.Model):
    state_name = models.ForeignKey(States)
    dist_name = models.ForeignKey(Districts)
    block_name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        verbose_name = ('Block')
        verbose_name_plural = ('Block\'s')

    def __str__(self):
        return self.block_name

class Panchayats(models.Model):
    state_name = models.ForeignKey(States)
    dist_name = models.ForeignKey(Districts)
    block_name = models.ForeignKey(Blocks)
    panchayat_name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        verbose_name = ('Panchayat')
        verbose_name_plural = ('Panchayats')

    def __str__(self):
        return self.panchayat_name

class Villages(models.Model):
    state_name = models.ForeignKey(States)
    dist_name = models.ForeignKey(Districts)
    block_name = models.ForeignKey(Blocks)
    panchayat_name = models.ForeignKey(Panchayats)
    village_name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        verbose_name = ('Village')
        verbose_name_plural = ('Villages')

    def __str__(self):
        return self.village_name




class Dealer_Registration(models.Model):
    shop_name = models.CharField(max_length=255)
    licence_num = models.CharField(max_length=255)
    company_types_list = (
        ('private', 'PRIVATE'),
        ('pacs', 'PACS'),
    )
    company_type = models.CharField(max_length=7, choices=company_types_list)
    dealer_name = models.CharField(max_length=255)
    contact_num = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])
    address = models.TextField(max_length=255)
    state_name = models.ForeignKey(States)
    dist_name = models.ForeignKey(Districts)
    block_name = models.ForeignKey(Blocks)
    spo_list = (
        ('spo1', 'SPO 1'),
        ('spo2', 'SPO 2'),
        ('spo3', 'SPO 3'),
    )
    dealer_spo = models.CharField(max_length=5, choices= spo_list)
    date = models.DateTimeField(default= datetime.now())
    dealer_pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(6)])

    #Meta CLASS
    class Meta:
        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealers')

    def __str__(self):
        return self.shop_name

class AAO_Registration(models.Model):
    aao_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])
    state_name = models.ForeignKey(States)
    dist_name = models.ForeignKey(Districts)
    block_name = models.ForeignKey(Blocks)

    #Meta Class
    class Meta:
        verbose_name = _('AAO')
        verbose_name_plural = _('AAOs')

    def __str__(self):
        return self.aao_name + '-' + self.block_name


class VAW_Registration(models.Model):
    VAW_name = models.CharField(max_length=255)
    VAW_contact_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])
    state_name = models.ForeignKey(States)
    dist_name = models.ForeignKey(Districts)
    block_name = models.ForeignKey(Blocks)
    panchayat_name = models.ForeignKey(Panchayats)

    #Meta Class
    class Meta:
        verbose_name = _('VAW')
        verbose_name_plural = _('VAWs')

    def __str__(self):
        return self.VAW_name

class STRVCategory(models.Model):
    def image_tag(self):
        return u'<img src="%s" />' %  '/home/ubuntu/irri-pracs/SeedCastfromGit/IRRI-Test/SeedCast/pics'

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    category_name = models.CharField(max_length=255)
    category_short_code = models.CharField(max_length=255)
    category_description = models.CharField(max_length=650)
    image = models.ImageField(upload_to="pics")

    #Meta Class
    class Meta:
        verbose_name = _('STRV Category')
        verbose_name_plural = _('STRV Category')

    def __str__(self):
        return self.category_short_code + '-' + self.category_name

class STRVVariety(models.Model):
    variety_name = models.CharField(max_length=255, primary_key=True)
    variety_code = models.CharField(max_length=255)
    description = models.TextField(max_length=650)
    duration_in_days = models.PositiveIntegerField()
    suitable_land_type = models.CharField(max_length=200)
    plant_height = models.PositiveIntegerField()
    grain_type = models.CharField(max_length=255)
    yield_in_tonne = models.PositiveIntegerField()

    #Meta Class
    class Meta:
        verbose_name = _('STRV Variety')
        verbose_name_plural = _('STRV Varieties')

    def __str__(self):
        return self.variety_name + '---' + self.variety_code


class Mobnum(models.Model):
    mobnum = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])

    class Meta:
        verbose_name = _('Mobile Number')
        verbose_name_plural = _('Mobile numbers')

    def __str__(self):
        return str(self.mobnum)

class VAWDemand(models.Model):
    village_name = models.ForeignKey(Villages)
    variety_name = models.ForeignKey(STRVVariety)
    quantity = models.PositiveIntegerField()
    date_collected = models.DateField(default=datetime.now())
    check = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'VAW-Demand'
        verbose_name_plural = 'VAW-Demands'

    def __str__(self):
        return self.village_name

class Demand(models.Model):
    variety_name = models.ForeignKey(STRVVariety)
    quantity = models.PositiveIntegerField()
    date_collected = models.DateField()
    chk = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Dealer Demand'
        verbose_name_plural = 'Dealer Demands'

    def __str__(self):
        return str(self.quantity)

class Pilotplots(models.Model):
    dist_name = models.ForeignKey(Districts)
    block_name = models.ForeignKey(Blocks)
    panchayat_name = models.ForeignKey(Panchayats)

    class Meta:
        verbose_name = 'Pilot Plots'

    def __str__(self):
        return self.panchayat_name

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])
    email = models.EmailField(blank=True)
    suggestion = models.TextField(max_length=1650)

    class Meta:
        verbose_name = 'Feedback'

    def __str__(self):
        return self.name



