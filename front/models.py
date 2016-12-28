from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class Contacte(models.Model):
    nom = models.CharField(max_length=80 , null=False)
    prenom = models.CharField(max_length=80 , null=False)
    message = models.TextField(null=True , blank=True)
    telephone = models.CharField(max_length=10 , validators=[RegexValidator(regex='^\d{10}$', message='Veuiller donner un téléphone valide', code='Invalid number')] , null=False)
    ville = models.CharField(max_length=90 , null=False)
    rue = models.CharField(max_length=120 , null=False)
    numero_de_la_voie = models.PositiveIntegerField( null=False)
    code_postal = models.IntegerField(max_length=5 , validators=[RegexValidator(regex='^\d{5}$', message='Veuiller donner un code postal valide', code='Invalid postal')] , null=False)
    mail = models.EmailField( blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de la demende")

    def __str__(self):

        return self.nom
