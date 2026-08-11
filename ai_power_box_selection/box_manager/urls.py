from django.urls import path

from box_manager.views import *

urlpatterns= [
        path('get/', box_manager.as_view())
        ]
