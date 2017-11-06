from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import request, Http404
from .models import Dealer_Registration, AAO_Registration, VAW_Registration, STRVCategory, STRVVariety, Mobnum, DealerDemand, Feedback, States, Districts, Blocks, Panchayats, Villages, Stock, VAWDemand, SPO
from .serializers import DealerSerializer, AAOSerializer, VAWSerializer, STRVCategorySerializer, STRVVarietySerializer, MobnumSerializer, DealerDemandSerializer, FeedbackSerializer, StatesSerializer, DistrictsSerializer, BlocksSerializer, PanchayatsSerializer, VillagesSerializer, StockSerializer, VAWDemandSerializer, SPOSerializer
from rest_framework import generics
from highcharts.views import HighChartsBarView
from highcharts.views import HighChartsPieView
from rest_framework import status


#Dealer's list
class DealerList(APIView):
    def get(self, request, format=None):
        dealer = Dealer_Registration.objects.all()
        serializer = DealerSerializer(dealer, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = DealerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dealer = self.get_object(pk)
        dealer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#AAO Registration Model view
class AAOList(generics.ListCreateAPIView):
    queryset = AAO_Registration.objects.all()
    serializer_class = AAOSerializer

class AAODetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AAO_Registration.objects.all()
    serializer_class = AAOSerializer


#VAW Registration Model View
class VAWList(generics.ListCreateAPIView):
    queryset = VAW_Registration.objects.all()
    serializer_class = VAWSerializer

class VAWDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VAW_Registration.objects.all()
    serializer_class = VAWSerializer



#STRV Category Model View
# class STRVCategoryList(generics.ListCreateAPIView):
#     queryset = STRVCategory.objects.all()
#     serializer_class = STRVCategorySerializer
#
# class STRVCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = STRVCategory.objects.all()
#     serializer_class = STRVCategorySerializer

class STRVCategoryList(APIView):

    def get(self, request, format=None):
        category = STRVCategory.objects.all()
        serializer = STRVCategorySerializer(category, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = STRVCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class STRVCategoryDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return STRVCategory.objects.get(pk=pk)
        except STRVCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        category = STRVCategorySerializer(category)
        return Response(category.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = STRVCategorySerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#STRV Variety Model view
class STRVVarietyList(APIView):

    def get(self, request, format=None):
        variety = STRVVariety.objects.all()
        serializer = STRVVarietySerializer(variety, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = STRVVarietySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        variety = self.get_object(pk)
        variety.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class STRVVarietyDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return STRVVariety.objects.get(pk=pk)
        except STRVVariety.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        category = STRVVarietySerializer(category)
        return Response(category.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = STRVVarietySerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        variety = self.get_object(pk)
        variety.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Mobile numbers model
class MobnumList(APIView):

    def get(self, request, format=None):
        mob = Mobnum.objects.all()
        serializer = MobnumSerializer(mob, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = MobnumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #Getting Dealer objects
            # dealer = list(Dealer_Registration.objects.all())
            # serializer2 = DealerSerializer(dealer, many=True)
            # print(dealer)
            # print("Serializer 2:" + serializer2)
            # if serializer in dealer:
            #     return Response(serializer2.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mobnum = self.get_object(pk)
        mobnum.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Chart View example...
class BarView(HighChartsBarView):
    categories = ['Orange', 'Bananas', 'Apples']

    # @property
    # def title(self):
    #     return 'This is a new Title for graphsview...'
    @property
    def series(self):
        result = []
        for name in ('Joe', 'Jack', 'William', 'Averell'):
            data = []
            for x in range(len(self.categories)):
                data.append(random.randint(0, 10))
            result.append({'name': name, "data": data})
        return render(request, 'graphs.html', context=result)

        # return result

#Dealer Demand model
class DealerDemandList(APIView):

    def get(self, request, format=None):
        demand = DealerDemand.objects.all()
        serializer = DealerDemandSerializer(demand, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = DealerDemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        demand = self.get_object(pk)
        demand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Stock available POST url
class StockList(APIView):

    # def get(self, request, format=None):
    #     demand = Stock.objects.all()
    #     serializer = StockSerializer(demand, many=True)
    #     return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        demand = self.get_object(pk)
        demand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Feedback post url
class FeedbackList(APIView):
    # def get(self, request, format=None):
    #     feedback = Feedback.objects.all()
    #     serializer = FeedbackSerializer(feedback, many=True)
    #     return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        feedback = self.get_object(pk)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StatesList(APIView):

    def get(self, request, format=None):
        state = Mobnum.objects.all()
        serializer = StatesSerializer(state, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = StatesSerializer(data=request.data)
        dealers = DealerSerializer(ddata = request.data)
        if serializer.is_valid():
            # serializer.save()
            if serializer in dealers:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        states = self.get_object(pk)
        states.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DistrictsList(APIView):

    def get(self, request, format=None):
        dist = Districts.objects.all()
        serializer = DistrictsSerializer(dist, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = DistrictsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dist = self.get_object(pk)
        dist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlocksList(APIView):

    def get(self, request, format=None):
        blocks = Blocks.objects.all()
        serializer = BlocksSerializer(blocks, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = BlocksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blocks = self.get_object(pk)
        blocks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PanchayatsList(APIView):

    def get(self, request, format=None):
        panchayats = Panchayats.objects.all()
        serializer = PanchayatsSerializer(panchayats, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = PanchayatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        panchayats = self.get_object(pk)
        panchayats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VillagesList(APIView):

    def get(self, request, format=None):
        villages = Villages.objects.all()
        serializer = VillagesSerializer(villages, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = VillagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        villages = self.get_object(pk)
        villages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#SPOs
class SPOList(generics.ListCreateAPIView):
    queryset = SPO.objects.all()
    serializer_class = SPOSerializer


class VAWDemandList(APIView):

    def get(self, request, format=None):
        vawdemand = VAWDemand.objects.all()
        serializer = VAWDemandSerializer(vawdemand, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = VAWDemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vaw = self.get_object(pk)
        vaw.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


