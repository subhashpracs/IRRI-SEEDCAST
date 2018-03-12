from datetime import datetime

from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext_lazy as _
from django import forms
# from jchart import Chart


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
<<<<<<< HEAD
        verbose_name_plural = _('Districts')
=======
        verbose_name_plural = _('District\'s')
>>>>>>> 97dc6007734f4106dbe23511c38c457bb2084a43

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
        verbose_name = _('Village')
        verbose_name_plural = _('Villages')

    def __str__(self):
        return self.village_name




class SPO(models.Model):
    spo = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = _('SPO')

    def __str__(self):
        return self.spo



class Dealer_Registration(models.Model):
    shop_name = models.CharField(max_length=255, blank=True)
    license_num = models.CharField(max_length=255, blank=True)
    company_types_list = (
        ('private', 'PRIVATE'),
        ('pacs', 'PACS'),
    )
    company_type = models.CharField(max_length=7, choices=company_types_list)
    dealer_name = models.CharField(max_length=255)
    contact_num = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)], null=True)
    address = models.TextField(max_length=255, blank=True)
    state_name = models.ForeignKey(States)
    dist_name = models.ForeignKey(Districts)
    block_name = models.ForeignKey(Blocks)
    dealer_spo = models.ForeignKey(SPO)
    date = models.DateTimeField(default= datetime.now())
    dealer_pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(6)], blank=True)

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
        return self.aao_name + '-' + str(self.block_name)


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

    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_short_code = models.CharField(max_length=255)
    category_description = models.TextField(max_length=650)
    image = models.ImageField(upload_to="static/imgs/uploaded/category")

    #Meta Class
    class Meta:
        verbose_name = _('STRV Category')
        verbose_name_plural = _('STRV Category')

    def __str__(self):
        return self.category_short_code

class STRVVariety(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.ForeignKey(STRVCategory)
    variety_name = models.CharField(max_length=255)
    variety_code = models.CharField(max_length=255)
    description = models.TextField(max_length=650)
    duration_in_days = models.CharField(max_length=20)
    suitable_land_type = models.CharField(max_length=200)
    plant_height = models.CharField(max_length=20)
    grain_type = models.CharField(max_length=255)
    yield_in_tonne = models.CharField(max_length=20)
    yield_advantage = models.CharField(max_length=50)


    #Meta Class
    class Meta:
        verbose_name = _('STRV Variety')
        verbose_name_plural = _('STRV Varieties')

    def __str__(self):
        return self.variety_name


class Mobnum(models.Model):
    mobnum = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])

    class Meta:
        verbose_name = _('Mobile Number')
        verbose_name_plural = _('Mobile numbers')

    def __str__(self):
        return str(self.mobnum)


class Vawmobnum(models.Model):
    vaw_num = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])

    class Meta:
        verbose_name = _('VawMobile')
        verbose_name_plural = _('VawMobile Numbers')

    def __str__(self):
        return str(self.vaw_num)

class Varietynew(models.Model):
    category = models.IntegerField()


    def __str__(self):
        return str(self.category)


class VAWDemand(models.Model):
    vaw = models.ForeignKey(VAW_Registration, db_column='VAW_Registration_id')
    village_name = models.CharField(max_length=255)
    variety_name = models.ForeignKey(STRVVariety)
<<<<<<< HEAD
    varietyName = models.CharField(max_length=100)
=======
    variety2 = models.CharField(max_length=100)
>>>>>>> 97dc6007734f4106dbe23511c38c457bb2084a43
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

class Stock(models.Model):
    dealer_shop = models.ForeignKey(Dealer_Registration, db_column='Dealer_Registration_id')
    variety_name = models.ForeignKey(STRVVariety)
    available = models.PositiveIntegerField()
    date_wn_available = models.DateField()
    check = models.BooleanField()


    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return str(self.variety_name)

class Pilotplots(models.Model):
    farmer_name = models.CharField(max_length=255)
    contact_num = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])
    dist_name = models.ForeignKey(Districts)
    block_name = models.ForeignKey(Blocks)
    panchayat_name = models.ForeignKey(Panchayats)
    village = models.CharField(max_length=255)
    variety = models.ForeignKey(STRVVariety)


    class Meta:
        verbose_name = 'Pilot Plots'

    def __str__(self):
        return str(self.dist_name)

class Plotsnew(models.Model):
    dist_name =  models.ForeignKey(Districts)
    block_name = models.ForeignKey(Blocks)
    panchayat_name = models.ForeignKey(Panchayats)

    class Meta:
        verbose_name = "Plots Post"


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])
    email = models.EmailField(blank=True)
    suggestion = models.TextField(max_length=1650)

    class Meta:
        verbose_name = 'Feedback'

    def __str__(self):
        return self.name


class ViewDealerlist(models.Model):
    district = models.ForeignKey(Districts)

    def __str__(self):
        return str(self.district)

class STRAvailability(models.Model):
    variety = models.ForeignKey(STRVVariety)
    #shop = models.ForeignKey(Dealer_Registration)

    def __str__(self):
        return str(self.variety)

# #Graphs...
# class Graph1(VAWDemand, models):
#     class Meta:
#         proxy = True
#         verbose_name = 'Variety wise Demand'
#         verbose_name_plural = 'Variety wise Demands'
#
#
