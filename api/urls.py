from django.urls import path
from api.views import EndPointDWH

urlpatterns = [
    path('', EndPointDWH.as_view()),
]