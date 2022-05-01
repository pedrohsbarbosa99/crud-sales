from django.urls import path

from crud_sales.djninja.api import api

urlpatterns = [path("", api.urls)]
