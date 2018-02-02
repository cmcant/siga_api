
from django.contrib import admin
from django.conf.urls import url, include
from serializer import *

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^api-auth/', include('rest_framework.urls')),   
]