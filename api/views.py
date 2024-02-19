from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from app.models import Club, Player, City, D_CLUB, D_SEX, D_AGEGRP, D_ETABLISHEMENT, D_DATE, F_PLAYER
from api.serializers import Club_Serializer, Player_Serializer, City_Serializer, D_CLUB_Serializer, D_SEX_Serializer, D_AGEGRP_Serializer, D_ETABLISHEMENT_Serializer, D_DATE_Serializer, F_PLAYER_Serializer

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

class API_Datawarehouse_D_DATE(BaseAPI):
    """API for D_DATE model."""
    model = D_DATE
    serializer_class = D_DATE_Serializer
    default_t = 'D_DATE'

class API_Datawarehouse_D_SEX(BaseAPI):
    """API for D_SEX model."""
    model = D_SEX
    serializer_class = D_SEX_Serializer
    default_t = 'D_SEX'

class API_Datawarehouse_D_AGEGRP(BaseAPI):
    """API for D_AGEGRP model."""
    model = D_AGEGRP
    serializer_class = D_AGEGRP_Serializer
    default_t = 'D_AGEGRP'

class API_Datawarehouse_D_CLUB(BaseAPI):
    """API for D_CLUB model."""
    model = D_CLUB
    serializer_class = D_CLUB_Serializer
    default_t = 'D_CLUB'

class API_Datawarehouse_D_ETABLISHEMENT(BaseAPI):
    """API for D_ETABLISHEMENT model."""
    model = D_ETABLISHEMENT
    serializer_class = D_ETABLISHEMENT_Serializer
    default_t = 'D_ETABLISHEMENT'

class API_Store_City(APIView, PageNumberPagination):
    page_size = 5
    lookup_field = 'postal_code'

    def get(self, request, postal_code=None):
        if postal_code is not None:
            data = City.objects.filter(postal_code=postal_code)
            serializer = City_Serializer(data=data, many=True)
        else:
            
            data = City.objects.all()
            serializer = City_Serializer(data=data, many=True)
        serializer.is_valid()

        result = {
            'count': City.objects.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)

    def post(self, request, postal_code=None):
        data = request.data
        serializer = City_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, postal_code=None):
        try:
            city = City.objects.get(postal_code=postal_code)
        except City.DoesNotExist:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = City_Serializer(city, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, postal_code=None):
        try:
            city = City.objects.get(postal_code=postal_code)
        except City.DoesNotExist:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = City_Serializer(city, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, postal_code=None):
        if postal_code is not None:
            data = City.objects.filter(postal_code=postal_code)
            if data.exists():
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "City not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Delete all City objects if no postal_code is provided
            City.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    # Recherche par nom de ville
    def search_by_name(self, request, city_name):
        data = City.objects.filter(name__icontains=city_name)
        serializer = City_Serializer(data=data, many=True)

        result = {
            'count': data.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)

