# Phase d'importations
from django.db import models
from django.utils import timezone
#création du formulaire de contact
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) #utilisateurs
    title = models.CharField(max_length=200) #longueur du texte
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)#date d'envoi
    published_date = models.DateTimeField(# date de publication
        blank=True, null=True)
    #fonctions de publication
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
         return self.title #retourner le titre du formulaire d'envoi
