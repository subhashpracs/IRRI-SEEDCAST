from rest_framework import serializers
from .models import Dealer_Registration, AAO_Registration, VAW_Registration, STRVCategory, STRVVariety, Mobnum, Demand, Feedback, States, Districts, Blocks, Panchayats, Villages

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer_Registration
        fields = '__all__'

class AAOSerializer(serializers.ModelSerializer):
    class Meta:
        model = AAO_Registration
        fields = '__all__'


class VAWSerializer(serializers.ModelSerializer):
    class Meta:
        model = VAW_Registration
        fields = '__all__'


class STRVCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = STRVCategory
        fields = '__all__'

class STRVVarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = STRVVariety
        fields = '__all__'


class MobnumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobnum
        fields = '__all__'

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'



class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '_all__'

class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'

class BlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocks
        fields = '__all__'

class PanchayatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panchayats
        fields = '__all__'

class VillagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villages
        fields = '__all__'
