from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class EndPointDWH(APIView):
    """_summary_

    Args:
        APIview (_type_): _description_
    """
    def get_club(self):
        return Response({'Result': ['ok']})