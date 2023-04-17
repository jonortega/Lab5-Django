from django.db import models

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
    id = models.IntegerField(primary_key=True)
    erabiltzailea_id = models.IntegerField()