from django.db import models
from django.contrib.auth.models import User

class Filma(models.Model):
    izenburua = models.CharField(max_length=255)
    zuzendaria = models.CharField(max_length=255)
    urtea = models.CharField(max_length=4)
    generoa = models.CharField(max_length=2)
    sinopsia = models.TextField()
    bozkak = models.IntegerField(default=0)

    def __str__(self):
        return self.izenburua

class Bozkatzailea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class FilmaBozkatzailea(models.Model):
    filma = models.ForeignKey(Filma, on_delete=models.CASCADE)
    bozkatzailea = models.ForeignKey(Bozkatzailea, on_delete=models.CASCADE)
    bozkak = models.IntegerField(default=0)

    class Meta:
        unique_together = ('filma', 'bozkatzailea')

