from django.core.serializers import json
from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import request, Http404

from Reports.models import VAWDemand, DealerDemand
from .models import Dealer_Registration, AAO_Registration, VAW_Registration, STRVCategory, STRVVariety, Mobnum, Feedback, States, Districts, Blocks, Panchayats, Villages, Stock, SPO, Vawmobnum, Varietynew, ViewDealerlist, Pilotplots, STRAvailability, Plotsnew
from .serializers import DealerSerializer, AAOSerializer, VAWSerializer, STRVCategorySerializer, STRVVarietySerializer, MobnumSerializer, DealerDemandSerializer, FeedbackSerializer, StatesSerializer, DistrictsSerializer, BlocksSerializer, PanchayatsSerializer, VillagesSerializer, StockSerializer, VAWDemandSerializer, SPOSerializer, VAWMobSerializer, VarietynewSerializer, ViewDealerSerializer, PlotsSerializer, STRAvailabilitySerializer, PilotplotsSerializer
from rest_framework import generics
from highcharts.views import HighChartsBarView
from highcharts.views import HighChartsPieView
from rest_framework import status
from django.http import JsonResponse
from django.views.generic import View
# from jchart import Chart


# class




User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)  # http response

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        variety_labels_vaw = VAWDemand.objects.all()
        varieties = []
        for obj in variety_labels_vaw:
            varieties.append(str(obj.variety_name))

        new_labels = varieties
        print("list is: " + str(varieties))
        demands = []
        for object in variety_labels_vaw:
            demands.append(object.quantity)

        #new_demands = demands

        print("Demands:" + str(demands))

        final_varieties = []
        varieties_index = []
        for i in varieties:
            if i not in final_varieties:
                final_varieties.append(i)
                varieties_index.append(varieties.index(i))

        print("Final varieties are:" + str(final_varieties))
        print("Final varieties indexes:" + str(varieties_index))

        k=0
        final_demand = [0]*len(final_varieties)

        excepted_indexes = []
        for i in range(0,len(varieties)):
            if i not in excepted_indexes:
                j = i+1
                count = 0
                while(j<len(varieties)):
                    if(varieties[i] == varieties[j]):
                        excepted_indexes.append(j)
                        if(count==0):
                            final_demand[k] = demands[i] + demands[j]
                            count+=1

                        else:
                            final_demand[k]+=demands[j]

                    else:
                        pass
                        # print("Nothing here...in while")

                    j=j+1

                k=k+1

            else:
                pass
              #  print("Nothing in excepted_indexes...")


            for i in range(0, len(final_demand)):
                if(final_demand[i]==0):
                    final_demand[i]+=demands[varieties_index[i]]

                else:
                    pass

       # print("The logic is checking here...:" + "Final varieties:"+ str(final_varieties) + "\n \t Final Demands...:" + str(final_demand))

        data = {
            "labels": final_varieties,
            "default": final_demand,
        }

        data2 = {
            "labels2": ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"],
            "default2": [qs_count, 23, 2, 3, 12, 2]
        }


        return Response(data)



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

class VAWDetail(APIView):
    def get_object(self, pk):
        try:
            return VAW_Registration.objects.get(pk=pk)
        except VAW_Registration.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vaw = self.get_object(pk)
        vaw = VAWSerializer(vaw)
        return Response(vaw.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = VAWSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#STRV Category
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

#STRV Variety Model view
class STRVVarietyList(APIView):

    ser = STRVVarietySerializer

    # def get_queryset(self):
    #     category_name = self.kwargs['category_name']
    #     return STRVVariety.objects.filter(category_name=category_name)

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

#STRVVariety list as category under...
class STRVVarietyNew(APIView):
    # def get(self,request):
    #     category_name = STRVCategory.objects.all()
    #     variety = STRVVariety.objects.filter(category_name=category_name)
    #     serializer_class = STRVVarietySerializer(variety, many=True)
    #     return Response(serializer_class.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = VarietynewSerializer(data=request.data)
        if serializer.is_valid():
            print("Serializer:" + str(serializer.data))
            posted_category = serializer.data['category']
            queryset = STRVVariety.objects.filter(category_name=posted_category)
            variety_list = []
            for obj in queryset:
                variety = obj.variety_name
                variety_ori = obj.variety_name_oriya
                varietycode = obj.variety_code
                descriptionn = obj.description
                description_ori = obj.description_oriya
                duration = obj.duration_in_days
                land = obj.suitable_land_type
                land_ori = obj.suitable_land_type_oriya
                height = obj.plant_height
                grain = obj.grain_type
                grain_ori = obj.grain_type_ori
                yieldin = obj.yield_in_tonne
                advantage = obj.yield_advantage
                category = obj.category_name
                variety_dic = { "variety_name" : variety, "variety_name_oriya" : variety_ori, "variety_code" : varietycode, "description" : descriptionn, "description_oriya" : description_ori, "duration_in_days" : duration, "suitable_land_type" : land, "suitable_land_type_oriya" : land_ori, "plant_height" : height, "grain_type" : grain, "grain_type_ori" : grain_ori, "yield_in_tonne" : yieldin, "yield_advantage" : advantage }
                variety_list.append(variety_dic,)

            print("Variety List:" + str(variety_list))
            return Response(variety_list, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

#Mobile numbers model
class MobnumList(APIView):

    # def get(self, request, format=None):
    #     mob = Mobnum.objects.all()
    #     serializer = MobnumSerializer(mob, many=True)
    #     return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = MobnumSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            mob_posted = serializer.data['mobnum']
            queryset = Dealer_Registration.objects.all()
            dealers = []
            mobile_numbers_list = []
            for obj in queryset:
                mob_num = obj.contact_num
                mobile_numbers_list.append(mob_num)
                #dealer_list = { "dealer_name" : obj.dealer_name, "license" : obj.license_num, "contact" : obj.contact_num, "block" : obj.block_name }
                dealer_list = { "id" : obj.id }
                dealers.append(dealer_list,)

            if mob_posted in mobile_numbers_list:
                mob_index = mobile_numbers_list.index(mob_posted)
                print("Mobile number matched...")
                return Response(dealers[mob_index], status=status.HTTP_200_OK)
            else:
                print("Mobile number not found...")
                no_dealer_data = { "error_msg" : "Not registered...", }
                return Response(no_dealer_data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ViewDealer(APIView):

    @csrf_exempt
    def post(self, request, format=None):
        serializer = ViewDealerSerializer(data=request.data)
        if serializer.is_valid():
            dist_posted = serializer.data['district']
            queryset = Dealer_Registration.objects.filter(dist_name=dist_posted)
            print("Length of queryset queried is:" + str(len(queryset)))
            query_length = len(queryset)
            dealer_dist_wise = []
            for obj in queryset:
                dealer_list = { "dealer_name" : obj.dealer_name, "contact" : obj.contact_num, "license" : obj.license_num, "shop" : obj.shop_name }
                dealer_dist_wise.append(dealer_list,)


            if query_length == 0:
                return Response( { "error" : "No data found..." }, status=status.HTTP_204_NO_CONTENT)

            else:
                return Response(dealer_dist_wise, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlotsBlocks(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        serializer = PlotsSerializer(data=request.data)
        if serializer.is_valid():
            dist_posted = serializer.data['dist_name']
            blocks = Panchayats.objects.filter(dist_name=dist_posted)
            blocks_list = []
            for i in blocks:
                blocks_list.append(i.block_name)

            return Response(blocks_list, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlotsPanchayat(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        serializer = PlotsSerializer(data=request.data)
        if serializer.is_valid():
            dist_posted = serializer.data['block_name']
            blocks = Panchayats.objects.filter(dist_name=dist_posted)
            blocks_list = []
            for i in blocks:
                blocks_list.append(i.block_name)

            return Response(blocks_list, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Plots(APIView):


    # def get(self, request, format=None):
    #     plotsall = Pilotplots.objects.all()
    #     serializer = PlotsSerializer(plotsall, many=True)
    #     return Response(serializer.data)
    #

    @csrf_exempt
    def post(self, request, format=None):
        serializer = PlotsSerializer(data=request.data)
        if serializer.is_valid():
            dist_posted = serializer.data['dist_name']
            block_posted = serializer.data['block_name']
            panchayat_posted = serializer.data['panchayat_name']
            queryset = Pilotplots.objects.filter(dist_name=dist_posted,block_name=block_posted, panchayat_name=panchayat_posted)
            farmer_list_dbp_wise = []
            for obj in queryset:
                farmer_list = { "farmer" : obj.farmer_name, "contact" : obj.contact_num }
                farmer_list_dbp_wise.append(farmer_list)
            print("Farmer List:" + str(farmer_list_dbp_wise))

            length_farmer_list = len(farmer_list_dbp_wise)

            if(length_farmer_list==0):
                return Response( { "no_data" : "No data found!!!" } , status=status.HTTP_204_NO_CONTENT)

            else:
                return Response(farmer_list_dbp_wise, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlotsDetails(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return Pilotplots.objects.get(pk=pk)
        except Pilotplots.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        plots = self.get_object(pk)
        plot = PilotplotsSerializer(plots)
        return Response(plot.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = PilotplotsSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#VAW Mobile numbers...
class VAWMobileList(APIView):

    # def get(self, request, format=None):
    #     mob = Mobnum.objects.all()
    #     serializer = MobnumSerializer(mob, many=True)
    #     return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        serializer = VAWMobSerializer(data=request.data)
        if serializer.is_valid():
            mob_posted = serializer.data['vaw_num']
            queryset = VAW_Registration.objects.all()
            vaws = []
            mobile_numbers_list = []
            for obj in queryset:
                mob_num = obj.VAW_contact_number
                mobile_numbers_list.append(mob_num)
                vaw_list = { "id" : obj.id }
                vaws.append(vaw_list, )

            if mob_posted in mobile_numbers_list:
                mob_index = mobile_numbers_list.index(mob_posted)
                print("Mobile number matched...")
                return Response(vaws[mob_index], status=status.HTTP_200_OK)
            else:
                print("Mobile number not found...")
                no_vaw_data = { "error_message" : "No VAW for this number..." }
                return Response(no_vaw_data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

#Stock available POST url
class StockList(APIView):

    def get(self, request, format=None):
        demand = Stock.objects.all()
        serializer = StockSerializer(demand, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class StatesList(APIView):

    def get(self, request, format=None):
        state = States.objects.all()
        serializer = StatesSerializer(state, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = StatesSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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



class STRVAvailability(APIView):

    @csrf_exempt
    def post(self, request, format=None):
        serializer = STRAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            print("Serializer data:" + str(serializer.data))
            variety_posted = serializer.data['variety']
            #shop_from_stocks = serializer.data['shop']
            #dealer_details = Dealer_Registration.objects.filter(id=shop_from_stocks)
            #availability = Stock.objects.filter(variety_name=variety_posted)
            dealer_list = []
            dealer_ids = []
            availability = []
            #sub_dealer_list = {}
            queryset1 = Stock.objects.filter(variety_name=variety_posted)
            for obj1 in queryset1:
                dealer_ids.append(obj1.id)

            for obj2 in queryset1:
                availability.append(obj2.available)

            for obj3 in dealer_ids:
                queryset2 = Dealer_Registration.objects.filter(id=obj3)
                sub_dealer_list = {}
                for obj4 in queryset2:
                    sub_dealer_list['dealer'] = obj4.dealer_name
                    sub_dealer_list['contact'] = obj4.contact_num

                for obj5 in availability:
                    sub_dealer_list['available'] = obj5

                dealer_list.append(sub_dealer_list)


            # print("Availability2 is: " + str(availability))
            #for obj2 in availability:
            #    dealer_list['available_from'] = obj2.available
                # print("Available is:" + str(availability2))
            # availability2 = availability.available

            #print("Length of queryset queried is:" + str(len(dealer_details)))
            query_length = len(availability)
            #print("Dealer Details:" + str(dealer_details))
            #print("shop:" + str(shop_from_stocks))
            dealer_stock_wise = []
            #for obj in dealer_details:
                # dealer_list = { "dealer_name" : obj.dealer_name, "contact" : obj.contact_num, "shop_name" : obj.shop_name }
             #   dealer_list['dealer_name'] = obj.dealer_name
             #   dealer_list['contact'] = obj.contact_num
              #  dealer_list['shop_name'] = obj.shop_name
                # dealer_list['available'] = availability2
              #  dealer_stock_wise.append(dealer_list,)


            if query_length == 0:
                return Response( { "error" : "No data found..." }, status=status.HTTP_204_NO_CONTENT)

            else:
                return Response(dealer_list, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


