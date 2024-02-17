from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from app.models import Club, Player, D_CLUB, D_SEX, D_AGEGRP, D_ETABLISHEMENT, D_DATE, F_PLAYER
from api.serializers import Club_Serializer, Player_Serializer, D_CLUB_Serializer, D_SEX_Serializer, D_AGEGRP_Serializer, D_ETABLISHEMENT_Serializer, D_DATE_Serializer, F_PLAYER_Serializer

class BaseAPI(APIView):
    """Base class for API views."""
    model = None
    serializer_class = None
    default_t = 'D_DATE'

    def get(self, request, pk=None):
        t = request.GET.get('t', None)
        if t:
            try:
                data = eval(t).objects.all()
                count = data.count()
            except AttributeError:
                return Response(data={'error': f'Model {t} not found.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            t = 'D_DATE'
            data = F_PLAYER.objects.all()
            count = data.count()

        serializer = eval(f"{t}_Serializer")(data=data, many=True)
        serializer.is_valid()

        result = {
            't': t,
            'count': count,
            'data': serializer.data,
        }

        return Response(data=result, status=status.HTTP_200_OK)

class API_Operational_Data_Store_Club(BaseAPI):
    """API for Club model."""
    model = Club
    serializer_class = Club_Serializer
    default_t = 'Club'

class API_Operational_Data_Store_Player(BaseAPI):
    """API for Player model."""
    model = Player
    serializer_class = Player_Serializer
    default_t = 'Player'

class API_Datawarehouse_F_PLAYER(BaseAPI):
    """API for F_PLAYER model."""
    model = F_PLAYER
    serializer_class = F_PLAYER_Serializer
    default_t = 'F_PLAYER'

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
