from django.db import models
from django.contrib.auth.models import User


class Muallif(models.Model):
    ism = models.CharField(max_length=111)
    yosh = models.PositiveSmallIntegerField()
    kasb = models.CharField(max_length=222)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Mualliflar'
    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=111)
    sana = models.DateTimeField(auto_now_add=True)
    mavzu = models.CharField(max_length=111)
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Maqolalar'

    def __str__(self):
        return self.sarlavha