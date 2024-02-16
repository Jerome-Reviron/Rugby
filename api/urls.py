from django.urls import path
from api.views import API_Operational_Data_Store, API_Datawarehouse

urlpatterns = [
    path('ODS/', API_Operational_Data_Store.as_view()),
    path('DWH/', API_Datawarehouse.as_view()),
]