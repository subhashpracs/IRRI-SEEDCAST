from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import request, Http404
from .models import Dealer_Registration, AAO_Registration, VAW_Registration, STRVCategory, STRVVariety, Mobnum, Demand, Feedback, States, Districts, Blocks, Panchayats, Villages
from .serializers import DealerSerializer, AAOSerializer, VAWSerializer, STRVCategorySerializer, STRVVarietySerializer, MobnumSerializer, DemandSerializer, FeedbackSerializer, StatesSerializer, DistrictsSerializer, BlocksSerializer, PanchayatsSerializer, VillagesSerializer
from rest_framework import generics
from highcharts.views import HighChartsBarView
from highcharts.views import HighChartsPieView
from rest_framework import status

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

class DealerDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return Dealer_Registration.objects.get(pk=pk)
        except Dealer_Registration.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dealer = self.get_object(pk)
        dealer = DealerSerializer(dealer)
        return Response(dealer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = DealerSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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
class STRVCategoryList(generics.ListCreateAPIView):
    queryset = STRVCategory.objects.all()
    serializer_class = STRVCategorySerializer

class STRVCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = STRVCategory.objects.all()
    serializer_class = STRVCategorySerializer



#STRV Variety Model view
class STRVVarietyList(generics.ListCreateAPIView):
    queryset = STRVVariety.objects.all()
    serializer_class = STRVVarietySerializer

#Mobile numbers model

class MobnumList(APIView):

    def get(self, request, format=None):
        mob = Mobnum.objects.all()
        serializer = MobnumSerializer(mob, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = MobnumSerializer(data=request.data)
        dealers = DealerSerializer(ddata = request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer in dealers:
                return Response(serializer.ddata, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mobnum = self.get_object(pk)
        mobnum.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MobnumDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Mobnum.objects.get(pk=pk)
        except Mobnum.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        mob = self.get_object(pk)
        mob = MobnumSerializer(mob)
        return Response(mob.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = MobnumSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
# class DemandList(generics.ListCreateAPIView):
#     queryset = Demand.objects.all()
#     serializer_class = DemandSerializer


class DemandList(APIView):

    def get(self, request, format=None):
        demand = Demand.objects.all()
        serializer = MobnumSerializer(demand, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = DemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        demand = self.get_object(pk)
        demand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DemandDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Demand.objects.get(pk=pk)
        except Demand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        demand = self.get_object(pk)
        demand = MobnumSerializer(demand)
        return Response(demand.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = DemandSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Feedback post url
class FeedbackList(APIView):
    def get(self, request, format=None):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

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

class StatesDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return States.objects.get(pk=pk)
        except Mobnum.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        states = self.get_object(pk)
        states = StatesSerializer(states)
        return Response(states.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = StatesSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
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

class DistrictsDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Districts.objects.get(pk=pk)
        except Mobnum.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dist = self.get_object(pk)
        dist = MobnumSerializer(dist)
        return Response(dist.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = DistrictsSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
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

class BlocksDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Blocks.objects.get(pk=pk)
        except Blocks.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blocks = self.get_object(pk)
        blocks = BlocksSerializer(blocks)
        return Response(blocks.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = BlocksSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PanchayatsList(APIView):

    def get(self, request, format=None):
        panchayats = Panchayats.objects.all()
        serializer = MobnumSerializer(panchayats, many=True)
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

class PanchayatsDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Panchayats.objects.get(pk=pk)
        except Panchayats.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        panchayats = self.get_object(pk)
        panchayats = PanchayatsSerializer(panchayats)
        return Response(panchayats.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = PanchayatsSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
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

class VillagesDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Villages.objects.get(pk=pk)
        except Villages.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        villages = self.get_object(pk)
        villages = VillagesSerializer(villages)
        return Response(villages.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = VillagesSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

