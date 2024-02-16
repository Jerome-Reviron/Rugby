from django.shortcuts import render
import json
import sqlite3

from app.models import Club, Player
from app.models import D_CLUB, D_SEX, D_AGEGRP, D_ETABLISHEMENT, D_DATE
from app.models import F_PLAYER
from api.serializers import Club_Serializer, Player_Serializer
from api.serializers import D_CLUB_Serializer, D_SEX_Serializer, D_AGEGRP_Serializer, D_ETABLISHEMENT_Serializer, D_DATE_Serializer
from api.serializers import F_PLAYER_Serializer

from Rugby.settings import DATABASES

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class API_Operational_Data_Store(APIView):
    """ Voici l\'API de ma base de donnée
        Méthode GET :
        Méthode POST :
        Méthode PUT :
        Méthode PATCH :
        Méthode DELETE :
    """
    def get(self, request, pk=None):

        if 't' in request.GET:
            t = request.GET['t']
            data = eval(t).objects.all()
            count = data.count()
        else:
            t = 'Club'
            data = Club.objects.all()
            count = data.count()

        serializer = Club_Serializer(data=data, many=True)
        serializer.is_valid()

        data = serializer.data

        result = {
            'count': count,
            'data': data,
        }

        return Response(data=result, status=status.HTTP_200_OK)


class API_Operational_Data_Store(APIView):
    """ Voici l\'API de ma base de donnée
        Méthode GET :
        Méthode POST :
        Méthode PUT :
        Méthode PATCH :
        Méthode DELETE :
    """
    def get(self, request, pk=None):
        
        if 't' in request.GET:
            t = request.GET['t']
            data = eval(t).objects.all()
            count = data.count()
        else:
            t = 'Player'
            data = Player.objects.all()
            count = data.count()

        serializer = Player_Serializer(data=data, many=True)
        serializer.is_valid()

        data = serializer.data

        result = {
            'count': count,
            'data': data,
        }

        return Response(data=result, status=status.HTTP_200_OK)

class API_Datawarehouse(APIView):
    """ Voici l\'API de ma base de donnée

        Méthode GET :
        Méthode POST :
        Méthode PUT :
        Méthode PATCH :
        Méthode DELETE :
    """

    def get(self, request, pk=None):

        if 't' in request.GET:
            t = request.GET['t']
            data = eval(t).objects.all()
            count = data.count()
        else:
            t = 'F_PLAYER'
            data = F_PLAYER.objects.all()
            count = data.count()

        serializer = eval(f"{t}_Serializer")(data=data, many=True)
        serializer.is_valid()

        data = serializer.data

        result = {
            't': t,
            'count': count,
            'data': data,
        }

        return Response(data=result, status=status.HTTP_200_OK)

    # def post(self, request):
    #     result = {
    #         'message':'Voici les résultats trouvés',
    #         'data':[]
    #     }

    #     return Response(result, status=status.HTTP_200_OK)

    # def put(self, request, pk=None):
    #     result = {
    #         'message':'Voici les résultats trouvés',
    #         'data':[]
    #     }

    #     return Response(result, status=status.HTTP_200_OK)

    # def patch(self, request, pk=None):
    #     result = {
    #         'message':'Voici les résultats trouvés',
    #         'data':[]
    #     }

    #     return Response(result, status=status.HTTP_200_OK)

    # def delete(self, request, pk=None):

    #     rows = Club.objects.all()
    #     count = rows.count()
    #     rows.delete()

    #     rows = Player.objects.all()
    #     count = rows.count()
    #     rows.delete()

    #     rows = D_CLUB.objects.all()
    #     count = rows.count()
    #     rows.delete()

    #     rows = D_SEX.objects.all()
    #     count = rows.count()
    #     rows.delete()

    #     rows = D_AGEGRP.objects.all()
    #     count = rows.count()
    #     rows.delete()

    #     rows = D_ETABLISHEMENT.objects.all()
    #     count = rows.count()
    #     rows.delete()

    #     rows = D_DATE.objects.all()
    #     count = rows.count()
    #     rows.delete()


    #     rows = F_PLAYER.objects.all()
    #     count = rows.count()
    #     rows.delete()

    #     conn = sqlite3.connect(DATABASES['default']['NAME'])
    #     conn.execute("VACUUM")
    #     conn.close()

    #     result = {
    #         'message': f"{count} lignes ont été supprimées",
    #         'data': []
    #     }

    #     return Response(result, status=status.HTTP_200_OK)
