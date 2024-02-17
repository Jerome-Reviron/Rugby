from rest_framework import serializers
from app.models import Club, Player
from app.models import D_CLUB, D_SEX, D_AGEGRP, D_ETABLISHEMENT, D_DATE
from app.models import F_PLAYER

class Club_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class Player_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class D_CLUB_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_CLUB
        fields = '__all__'

class D_SEX_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_SEX
        fields = '__all__'

class D_AGEGRP_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_AGEGRP
        fields = '__all__'

class D_ETABLISHEMENT_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_ETABLISHEMENT
        fields = '__all__'

class D_DATE_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_DATE
        fields = '__all__'

class F_PLAYER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = F_PLAYER
        fields = '__all__'