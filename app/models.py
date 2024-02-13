from django.db import models

class Club(models.Model):
    """
    Modèle représentant un club dans le système.

    Attributes:
        code_commune (int): Code de la commune du club.
        commune (str): Nom de la commune du club.
        code_qpv (str): Code QPV du club.
        nom_qpv (str): Nom QPV du club.
        departement (str): Département du club.
        region (str): Région du club.
        statut_geo (str): Statut géographique du club.
        code (int): Code du club.
        federation (str): Fédération du club.
        clubs (int): Nombre de clubs associés.
        epa (int): EPA du club.
        total (int): Total du club.
    """
    code_commune = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    code_qpv = models.CharField(max_length=255, blank=True, null=True)
    nom_qpv = models.CharField(max_length=255, blank=True, null=True)
    departement = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    statut_geo = models.CharField(max_length=255)
    code = models.IntegerField()
    federation = models.CharField(max_length=255)
    clubs = models.IntegerField()
    epa = models.IntegerField()
    total = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return  f"{self.code_qpv} - {self.code} - {self.federation}"

class Player(models.Model):
    code_commune = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    code_qpv = models.CharField(max_length=255, blank=True, null=True)
    nom_qpv = models.CharField(max_length=255, blank=True, null=True)
    departement = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    statut_geo = models.CharField(max_length=255)
    code = models.IntegerField()
    federation = models.CharField(max_length=255)
    f_1_4_ans = models.IntegerField()
    f_5_9_ans = models.IntegerField()
    f_10_14_ans = models.IntegerField()
    f_15_19_ans = models.IntegerField()
    f_20_24_ans = models.IntegerField()
    f_25_29_ans = models.IntegerField()
    f_30_34_ans = models.IntegerField()
    f_35_39_ans = models.IntegerField()
    f_40_44_ans = models.IntegerField()
    f_45_49_ans = models.IntegerField()
    f_50_54_ans = models.IntegerField()
    f_55_59_ans = models.IntegerField()
    f_60_64_ans = models.IntegerField()
    f_65_69_ans = models.IntegerField()
    f_70_74_ans = models.IntegerField()
    f_75_79_ans = models.IntegerField()
    f_80_99_ans = models.IntegerField()
    f_nr = models.IntegerField()
    h_1_4_ans = models.IntegerField()
    h_5_9_ans = models.IntegerField()
    h_10_14_ans = models.IntegerField()
    h_15_19_ans = models.IntegerField()
    h_20_24_ans = models.IntegerField()
    h_25_29_ans = models.IntegerField()
    h_30_34_ans = models.IntegerField()
    h_35_39_ans = models.IntegerField()
    h_40_44_ans = models.IntegerField()
    h_45_49_ans = models.IntegerField()
    h_50_54_ans = models.IntegerField()
    h_55_59_ans = models.IntegerField()
    h_60_64_ans = models.IntegerField()
    h_65_69_ans = models.IntegerField()
    h_70_74_ans = models.IntegerField()
    h_75_79_ans = models.IntegerField()
    h_80_99_ans = models.IntegerField()
    h_nr = models.IntegerField()
    nr_nr = models.IntegerField()
    total = models.IntegerField()

    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.code_qpv} - {self.code} - {self.federation}"

# Table de fait
class F_CLUB(models.Model):
    F_code = models.CharField(max_length=255, primary_key=True)
    D_QPV_FK = models.ForeignKey('D_QPV', on_delete=models.CASCADE)
    D_CODE_COMMUNE_FK = models.ForeignKey('D_COMMUNE', on_delete=models.CASCADE)
    D_SEX_FK = models.ForeignKey('D_SEX', on_delete=models.CASCADE)
    D_AGEGRP_FK = models.ForeignKey('D_AGEGRP', on_delete=models.CASCADE)
    federation = models.CharField(max_length=255)
    nb_epa = models.IntegerField()
    nb_club = models.IntegerField()
    total_value = models.IntegerField()

# Tables de dimensions
class D_SEX(models.Model):
    sexcode = models.CharField(max_length=255, primary_key=True)

class D_AGEGRP(models.Model):
    AgeGrpLabel = models.CharField(max_length=255, primary_key=True)

class D_GEOPOSITION(models.Model):
    region = models.CharField(max_length=255, primary_key=True)
    departement = models.CharField(max_length=255)
    statut_geo = models.CharField(max_length=255)

class D_COMMUNE(models.Model):
    code_commune = models.CharField(max_length=255, primary_key=True)
    commune = models.CharField(max_length=255)

class D_QPV(models.Model):
    code_qpv = models.CharField(max_length=255, primary_key=True)
    nom_qpv = models.CharField(max_length=255)
