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
    code_commune = models.CharField(max_length=255, blank=True, null=True, default=None)
    commune = models.CharField(max_length=255, blank=True, null=True, default=None)
    code_qpv = models.CharField(max_length=255, blank=True, null=True, default=None)
    nom_qpv = models.CharField(max_length=255, blank=True, null=True, default=None)
    departement = models.CharField(max_length=255, blank=True, null=True, default=None)
    region = models.CharField(max_length=255, blank=True, null=True, default=None)
    statut_geo = models.CharField(max_length=255, blank=True, null=True, default=None)
    code = models.CharField(max_length=255, blank=True, null=True, default=None)
    federation = models.CharField(max_length=255, blank=True, null=True, default=None)
    clubs = models.CharField(max_length=255, blank=True, null=True, default=None)
    epa = models.CharField(max_length=255, blank=True, null=True, default=None)
    total = models.CharField(max_length=255, blank=True, null=True, default=None)

    def __str__(self) -> str:
        return  f"{self.code_qpv} - {self.code} - {self.federation}"

class Player(models.Model):
    code_commune = models.CharField(max_length=255, blank=True, null=True, default=None)
    commune = models.CharField(max_length=255, blank=True, null=True, default=None)
    code_qpv = models.CharField(max_length=255, blank=True, null=True, default=None)
    nom_qpv = models.CharField(max_length=255, blank=True, null=True, default=None)
    departement = models.CharField(max_length=255, blank=True, null=True, default=None)
    region = models.CharField(max_length=255, blank=True, null=True, default=None)
    statut_geo = models.CharField(max_length=255, blank=True, null=True, default=None)
    code = models.CharField(max_length=255, blank=True, null=True, default=None)
    federation = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_1_4_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_5_9_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_10_14_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_15_19_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_20_24_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_25_29_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_30_34_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_35_39_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_40_44_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_45_49_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_50_54_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_55_59_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_60_64_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_65_69_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_70_74_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_75_79_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_80_99_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    f_nr = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_1_4_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_5_9_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_10_14_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_15_19_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_20_24_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_25_29_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_30_34_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_35_39_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_40_44_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_45_49_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_50_54_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_55_59_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_60_64_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_65_69_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_70_74_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_75_79_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_80_99_ans = models.CharField(max_length=255, blank=True, null=True, default=None)
    h_nr = models.CharField(max_length=255, blank=True, null=True, default=None)
    nr_nr = models.CharField(max_length=255, blank=True, null=True, default=None)
    total = models.CharField(max_length=255, blank=True, null=True, default=None)

    def __str__(self) -> str:
        return f"{self.code_qpv} - {self.code} - {self.federation}"

class D_CLUB(models.Model):
    code_code_qpv_code_commune = models.CharField(max_length=100, unique=True, blank=True, null=True)
    code = models.IntegerField()
    code_qpv = models.CharField(max_length=20, blank=True, null=True, default=None)
    nom_qpv = models.CharField(max_length=255, blank=True, null=True, default=None)
    federation = models.CharField(max_length=255, blank=True, null=True, default=None)
    region = models.CharField(max_length=255, blank=True, null=True, default=None)
    departement = models.CharField(max_length=255, blank=True, null=True, default=None)
    nom_departement = models.CharField(max_length=255, blank=True, null=True, default=None)
    code_commune = models.CharField(max_length=20, blank=True, null=True, default=None)
    commune = models.CharField(max_length=150, blank=True, null=True, default=None)
    statut_geo = models.CharField(max_length=20, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        # Concaténer les champs pour créer la clé primaire
        self.code_code_qpv_code_commune = f"{self.code}-{self.code_qpv}-{self.code_commune}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.code} - {self.code_qpv} - {self.commune}"

class D_SEX(models.Model):
    SexCode = models.CharField(max_length=5, primary_key=True)

class D_AGEGRP(models.Model):
    AgeGrpLabel = models.CharField(max_length=15, primary_key=True)

class D_ETABLISHEMENT(models.Model):
    EtablishementLabel = models.CharField(max_length=10, blank=True, null=True, default=None)
    Nombre = models.CharField(max_length=10, blank=True, null=True, default=None)

    def __str__(self) -> str:
        return f"{self.EtablishementLabel} - {self.Nombre}"

class D_DATE(models.Model):
    Date = models.DateField(primary_key=True)

class F_PLAYER(models.Model):
    D_SEX_FK = models.ForeignKey('D_SEX', on_delete=models.CASCADE)
    D_AGEGRP_FK = models.ForeignKey('D_AGEGRP', on_delete=models.CASCADE)
    D_CLUB_FK = models.ForeignKey('D_CLUB', on_delete=models.CASCADE)
    D_DATE_FK = models.ForeignKey('D_DATE', on_delete=models.CASCADE)
    D_ETABLISHEMENT_FK = models.ForeignKey('D_ETABLISHEMENT', on_delete=models.CASCADE)
    Total_Club = models.IntegerField()
    Total_Player = models.IntegerField()
