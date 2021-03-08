# We have 2 api calls for each model(House, Thermostat,Room and Light).
# First url for each view is for Getting the list, Creating a new entry and adding to that list with the POST request.
# Second url is for getting a specific entry for that specific model and Updating it with the PUT request.

from django.conf.urls import include, url
from django.contrib import admin
from homes.api import HouseList,HouseDetail,ThermostatList,ThermostatDetail,RoomList,RoomDetail,LightList,LightDetail
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^api/house_list/$', HouseList.as_view(), name='house_list'),
    url(r'^api/house_list/(?P<name>[\w\- ]+)/$', HouseDetail.as_view(), name='house_detail'),
    url(r'^api/house_list/(?P<name>[\w\- ]+)/thermostat_list/$', ThermostatList.as_view(), name='thermostat_list'),
    url(r'^api/house_list/(?P<name>[\w\- ]+)/thermostat_list/(?P<name2>[\w\- ]+)/$', ThermostatDetail.as_view(), name='thermostat_detail'),
    url(r'^api/house_list/(?P<name>[\w\- ]+)/room_list/$', RoomList.as_view(), name='room_list'),
    url(r'^api/house_list/(?P<name>[\w\- ]+)/room_list/(?P<name2>[\w\- ]+)/$', RoomDetail.as_view(), name='room_detail'),
    url(r'^api/house_list/(?P<name>[\w\- ]+)/room_list/(?P<name2>[\w\- ]+)/light_list/$', LightList.as_view(), name='light_list'),
    url(r'^api/house_list/(?P<name>[\w\- ]+)/room_list/(?P<name2>[\w\- ]+)/light_list/(?P<name3>[\w\- ]+)/$', LightDetail.as_view(),name='light_list'),
]
