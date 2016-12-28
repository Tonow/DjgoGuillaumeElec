from django.db import models

class Contacte(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    message = models.TextField(null=True)
    telephone = models.PositiveIntegerField()
    ville = models.CharField(max_length=90)
    rue = models.CharField(max_length=120)
    numero_de_la_voie = models.PositiveIntegerField()
    code_postal = models.PositiveIntegerField()
    mail = models.EmailField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de la demende")

    def __str__(self):

        return self.nom
