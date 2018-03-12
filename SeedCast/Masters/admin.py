from django.contrib import admin
from import_export.admin import ImportExportModelAdmin#It is useful when using list filters
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from django.contrib.admin import register, ModelAdmin
<<<<<<< HEAD
=======
from import_export.instance_loaders import BaseInstanceLoader
from import_export import fields
#django-import-export
from jet.admin import CompactInline
>>>>>>> 97dc6007734f4106dbe23511c38c457bb2084a43
from import_export import resources
from Masters.models import Dealer_Registration,AAO_Registration, VAW_Registration, STRVCategory, STRVVariety, Mobnum, States, Districts, Blocks, Panchayats, Villages, VAWDemand, DealerDemand, Pilotplots, Feedback, Stock, VAWDemand, SPO


admin.site.site_header = 'SeedCast'

admin.site.site_title = 'IRRI-SeedCast'

admin.site.register(States)

<<<<<<< HEAD
=======
# @admin.register(Graph1)
# class Graph1Admin(ModelAdmin):
#     change_list_template = 'templates/charts2.html'
#     date_hierarchy = 'created'


>>>>>>> 97dc6007734f4106dbe23511c38c457bb2084a43


#Dealer Registration
class DealerResource(resources.ModelResource):
    class Meta:
        model = Dealer_Registration
        fields = ('id','shop_name', 'license_num', 'company_type', 'dealer_name', 'contact_num', 'address', 'state_name', 'dist_name', 'block_name', 'dealer_spo', 'date', 'dealer_pincode')
        export_order = ('id', 'shop_name', 'license_num', 'company_type', 'dealer_name', 'contact_num', 'address', 'state_name', 'dist_name', 'block_name', 'dealer_spo', 'date', 'dealer_pincode')


# @admin.register(Dealer_Registration)

# Exporting via List Filters...
class DealerAdmin(ImportExportActionModelAdmin):
     list_display = ('id', 'shop_name', 'license_num', 'company_type', 'dealer_name', 'contact_num', 'address', 'state_name', 'dist_name', 'block_name', 'dealer_spo', 'date', 'dealer_pincode',)
     search_fields = ('shop_name', 'dealer_name',)
<<<<<<< HEAD
     # list_per_page = 10
     resource_class = DealerResource
=======
     list_per_page = 10
     resource_class = DealerResource
     # inlines = [DealerInline]
>>>>>>> 97dc6007734f4106dbe23511c38c457bb2084a43


admin.site.register(Dealer_Registration, DealerAdmin)




#VAW Registration
class VAWResource(resources.ModelResource):
    class Meta:
        model = VAW_Registration
        fields = ('id', 'VAW_name', 'VAW_contact_number', 'state_name', 'dist_name', 'block_name', 'panchayat_name')
        export_order = ('id', 'VAW_name', 'VAW_contact_number', 'state_name', 'dist_name', 'block_name', 'panchayat_name')


class VAWAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'VAW_name', 'VAW_contact_number', 'state_name', 'dist_name', 'block_name', 'panchayat_name',)
    search_fields = ('VAW_contact_number', )
    resource_class = VAWResource

admin.site.register(VAW_Registration, VAWAdmin)



#AAO Registration
class AAOResource(resources.ModelResource):
    class Meta:
        model = AAO_Registration

class AAOAdmin(ModelAdmin):
    list_display = ('id', 'aao_name', 'contact_number', 'state_name', 'dist_name', 'block_name')
    search_fields = ('aao_name', 'contact_number')
    resource_class = AAOResource

admin.site.register(AAO_Registration, AAOAdmin)




#STRVCategory
class STRVCatResource(resources.ModelResource):
    class Meta:
        model = STRVCategory
        fields = ('id', 'category_name', 'category_short_code', 'category_description', 'image')

class STRVCatAdmin(ModelAdmin):
    list_display = ('id', 'category_name', 'category_short_code', 'category_description', 'image')
    search_fields = ('category_short_code',)
    resource_class = STRVCatResource
    list_display_links = ('category_name',)

admin.site.register(STRVCategory, STRVCatAdmin)


<<<<<<< HEAD
=======



>>>>>>> 97dc6007734f4106dbe23511c38c457bb2084a43
#STRV Variety...
class STRVVarietyResource(resources.ModelResource):
    class Meta:
        model = STRVVariety
        fields = ('id', 'category_name_get', 'variety_name', 'variety_code', 'description', 'duration_in_days', 'suitable_land_type', 'plant_height', 'grain_type', 'yield_in_tonne')

class STRVVarietyAdmin(ModelAdmin):
    list_display = ('id', 'category_name_get', 'variety_name', 'variety_code', 'description', 'duration_in_days', 'suitable_land_type', 'plant_height', 'grain_type', 'yield_in_tonne')
    search_fields = ('variety_name', 'variety_code',)
    resource_class = STRVVarietyResource

    def category_name_get(self, obj):
        return obj.category_name.category_name
    category_name_get.admin_order_field = 'category'
    category_name_get.short_description = 'Category'

admin.site.register(STRVVariety, STRVVarietyAdmin)


<<<<<<< HEAD
#VAW Demand
class VAWDemandResource(resources.ModelResource):
    class Meta:
        model = VAWDemand
        fields = ('vaw', 'varietyName', 'quantity',)


class VAWDemandAdmin(ModelAdmin):
    list_display = ('vaw', 'varietyName', 'quantity', 'date_collected',)
    resource_class = VAWDemandResource

admin.site.register(VAWDemand, VAWDemandAdmin)

=======
admin.site.register(VAWDemand)


>>>>>>> 97dc6007734f4106dbe23511c38c457bb2084a43
#Dealer Demand
class DealerDemandResource(resources.ModelResource):
    class Meta:
        model = DealerDemand
<<<<<<< HEAD
        fields = ('dealer', 'variety_name', 'quantity', 'date_collected', 'chk')


class DealerDemandAdmin(ModelAdmin):
    list_display = ('dealer', 'variety_name', 'quantity', 'date_collected',)
    resource_class = DealerDemandResource

admin.site.register(DealerDemand, DealerDemandAdmin)
=======
        fields = ('dealer_get', 'get_variety_name', 'quantity', 'date_collected', 'chk')


class DealerDemandAdmin(ModelAdmin):
    list_display = ('id', 'dealer_get', 'get_variety_name', 'quantity', 'date_collected', 'chk')
    resource_class = DealerDemandResource
    def dealer_get(self, obj1):
        return obj1.dealer.dealer_name
    dealer_get.admin_order_field = 'Dealer'
    dealer_get.short_description = 'Dealer...'


    def get_variety_name(self,obj):
        return obj.variety_name_variety_name
    get_variety_name.admin_order_field = 'variety'
    get_variety_name.short_description = 'Variety'

admin.site.register(DealerDemand)
>>>>>>> 97dc6007734f4106dbe23511c38c457bb2084a43

admin.site.register(Pilotplots)

admin.site.register(Feedback)


admin.site.register(Stock)


admin.site.register(SPO)



#Districts
class DistrictsResource(resources.ModelResource):
    class Meta:
        model = Districts
        exclude = ('id',)
        import_id_fields = ('state_name', 'dist_name')

class DistrictsAdmin(ImportExportActionModelAdmin):
    list_display = ('get_state', 'dist_name',)
    search_fields = ('dist_name',)
    list_filter = ('dist_name',)
    list_per_page = 10
    resource_class = DistrictsResource


    def get_state(self,obj):
        return obj.state_name.state_name
    get_state.admin_order_field = 'state'
    get_state.short_description = 'State'

admin.site.register(Districts, DistrictsAdmin)



#Blocks
class BlocksResource(resources.ModelResource):
    class Meta:
        model = Blocks
        exclude = ('id',)
        import_id_fields = ('state_name', 'dist_name', 'block_name')

class BlocksAdmin(ImportExportActionModelAdmin):
    list_display = ('get_state', 'get_district', 'block_name',)
    search_fields = ('block_name',)
    list_filter = ('block_name',)
    list_per_page = 10
    resource_class = BlocksResource


    def get_state(self,obj):
        return obj.state_name.state_name
    get_state.admin_order_field = 'state'
    get_state.short_description = 'State'


    def get_district(self, obj):
        return obj.dist_name.dist_name
    get_district.admin_order_field = 'district'
    get_district.short_description = 'District'

admin.site.register(Blocks, BlocksAdmin)


#Panchayats
class PanchayatsResource(resources.ModelResource):
    class Meta:
        model = Panchayats
        exclude = ('id',)
        import_id_fields = ('state_name', 'dist_name', 'block_name', 'panchayat_name')

class PanchayatsAdmin(ImportExportActionModelAdmin):
    list_display = ('get_state_name', 'get_district_name', 'get_block_name', 'panchayat_name',)
    search_fields = ('panchayat_name',)
    list_per_page = 1700
    resource_class = PanchayatsResource

    def get_state_name(self, obj):
        return obj.state_name.state_name
    get_state_name.admin_order_field = 'state'
    get_state_name.short_description = 'State'

    def get_district_name(self, obj):
        return obj.dist_name.dist_name
    get_district_name.admin_order_field = 'district'
    get_district_name.short_description = 'District'

    def get_block_name(self, obj):
        return obj.block_name.block_name
    get_block_name.admin_order_field = 'block'
    get_block_name.short_description = 'Block'

admin.site.register(Panchayats, PanchayatsAdmin)



#Villages...
class VillagesResource(resources.ModelResource):
    class Meta:
        model = Villages
        exclude = ('id',)
        import_id_fields = ('state_name', 'dist_name', 'block_name', 'panchayat_name', 'village_name')

class VillagesAdmin(ImportExportActionModelAdmin):
    list_display = ('get_state_name', 'get_dist_name', 'get_block_name', 'get_panchayat_name', 'village_name')
    search_fields = ('village_name',)
    list_per_page = 6
    resource_class = VillagesResource

    def get_state_name(self, obj):
        return obj.state_name.state_name
    get_state_name.admin_order_field = 'state'
    get_state_name.short_description = 'State'

    def get_dist_name(self, obj):
        return obj.dist_name.dist_name
    get_dist_name.admin_order_field = 'district'
    get_dist_name.short_description = 'District'

    def get_block_name(self, obj):
        return obj.block_name.block_name
    get_block_name.admin_order_field = 'block'
    get_block_name.short_description = 'Block'

    def get_panchayat_name(self, obj):
        return obj.panchayat_name.panchayat_name
    get_panchayat_name.admin_order_field = 'panchayat'
    get_panchayat_name.short_description = 'Panchayat'


admin.site.register(Villages, VillagesAdmin)

<<<<<<< HEAD
=======
#Report Builder
# class ReportBuilder:
#     fields = (
#     'id', 'shop_name', 'license_num', 'company_type', 'dealer_name', 'contact_num', 'address', 'state_name', 'dist_name','block_name', 'spo', 'date', 'pincode')
#

>>>>>>> 97dc6007734f4106dbe23511c38c457bb2084a43

admin.site.index_title = 'Admin Panel'


admin.site.site_url = False
