from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from import_export import resources

from Reports.models import VAWDemand, DealerDemand


class VAWDemandResource(resources.ModelResource):
    class Meta:
        model = VAWDemand
        fields = ('vaw', 'varietyName', 'quantity',)


class VAWDemandAdmin(ModelAdmin):
    list_display = ('vaw', 'varietyName', 'quantity', 'date_collected',)
    resource_class = VAWDemandResource

admin.site.register(VAWDemand, VAWDemandAdmin)

#Dealer Demand
class DealerDemandResource(resources.ModelResource):
    class Meta:
        model = DealerDemand
        fields = ('dealer', 'variety_name', 'quantity', 'date_collected', 'chk')


class DealerDemandAdmin(ModelAdmin):
    list_display = ('dealer', 'variety_name', 'quantity', 'date_collected',)
    resource_class = DealerDemandResource

admin.site.register(DealerDemand, DealerDemandAdmin)
