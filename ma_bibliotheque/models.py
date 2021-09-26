from django.db import models

# Create your models here.

class Auteur(models.Model):
    id_auteur = models.AutoField(primary_key=True)
    nom_auteur = models.CharField(max_length=225)
    adr_auteur = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_auteur


class Editeur(models.Model):
    id_edit = models.AutoField(primary_key=True)
    nom_edit = models.CharField(max_length=225)
    adr_edit = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_edit

class Rayon(models.Model):
    id_rayon = models.AutoField(primary_key=True)
    num_rayon = models.IntegerField()
    loc_rayon = models.CharField(max_length=50)

    def __str__(self):
        return "Rayon {}".format(self.num_rayon)



class Theme(models.Model):
    id_theme = models.AutoField(primary_key=True)
    libelle_th = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle_th



class Mot_Cle(models.Model):
    id_mot_cle = models.AutoField(primary_key=True)
    libelle_mot = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle_mot
    


class Abonné(models.Model):
    id_abonne = models.AutoField(primary_key=True)
    nom_abonné = models.CharField(max_length=250)
    adr_abonné = models.CharField(max_length=250)
    tel_abonné = models.CharField(max_length=15)
    date_adh = models.DateField(auto_now_add=True)
    date_nais = models.DateField()
    cat_prof = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_auteur
    


class Pret(models.Model):
    id_pret = models.AutoField(primary_key=True)
    date_dem_pret = models.DateField(auto_now_add=True)
    date_pret = models.DateField()
    date_depot = models.DateField()
    date_retour = models.DateField()
    id_abonne = models.ForeignKey()

    def __str__(self):
        return "Date de demande : {} \nDate de prêt : {} \nDate de retour : {}".format(date_dem_pret, date_pret, date_retour)


class Livre(models.Model):
    id_livre = models.AutoField(primary_key=True)
    code_livre = models.CharField(max_length=50, unique=True)
    nom_livre = models.CharField(max_length=100)
    id_rayon = models.ForeignKey()
    mots_clés = models.ManyToManyField(Mot_Cle)
    themes = models.ManyToManyField(Theme)
    auteur = models.ManyToManyField(Auteur)

    def __str__(self):
        return "{} de {}".format(self.nom_livre, self.auteur)


class Exemplaire(models.Model):
    id_exemplaire = models.AutoField(primary_key=True)
    cote_livre = models.CharField(max_length=50, unique=True)
    etat_usure = models.CharField(max_length=50)
    id_edit = models.ForeignKey()
    id_pret = models.ForeignKey()
    id_livre = models.ForeignKey()

    def __str__(self):
        return "{} édité par {}".format(self.livre, self.editeur)
