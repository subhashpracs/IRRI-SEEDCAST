from import_export import resources
from import_export.instance_loaders import BaseInstanceLoader

from Masters.models import Dealer_Registration

class DealerResource(resources.ModelResource):
    class Meta:
        model = Dealer_Registration
#         instance_loader_class = MyCustomInstanceLoaderClass
#
# class MyCustomInstanceLoaderClass(BaseInstanceLoader):
#     def get_instance(self, row):
#         # your implementation here
#         return False

# def get_instance(self, row):
#     return False