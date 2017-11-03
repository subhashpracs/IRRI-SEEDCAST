from django.conf.urls import url, include
from Masters import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # url(r'^dealer_list/(?P<pk>[0-9]+)/$', views.DealerList.as_view()),
    url(r'^aao_list/$',views.AAOList.as_view()),
    url(r'^dealer_list/$', views.DealerList.as_view()),
    url(r'^vaw_list/$', views.VAWList.as_view()),
    url(r'^strv_category/$', views.STRVCategoryList.as_view()),
    url(r'^strv_variety/$', views.STRVVarietyList.as_view()),
    url(r'^mob', views.MobnumList.as_view()),
    url(r'^mob/(?P<pk>[0-9]+)/$', views.MobnumDetail.as_view()),
    url(r'^demand/$', views.DemandList.as_view()),
    url(r'^states/$', views.StatesList.as_view()),
    url(r'^districts/$', views.DistrictsList.as_view()),
    url(r'^blocks/$', views.BlocksList.as_view()),
    url(r'^panchayats/$', views.PanchayatsList.as_view()),
    url(r'^villages/$', views.VillagesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
