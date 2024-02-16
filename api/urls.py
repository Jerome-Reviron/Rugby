from django.urls import path
from api.views import API_Operational_Data_Store_Club, API_Operational_Data_Store_Player, API_Datawarehouse_F_PLAYER

urlpatterns = [
    path('ODS_Club/', API_Operational_Data_Store_Club.as_view()),
    path('ODS_Player/', API_Operational_Data_Store_Player.as_view()),
    path('DWH/', API_Datawarehouse_F_PLAYER.as_view()),
]