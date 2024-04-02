from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    powers = models.TextField(max_length=250)
    affiliation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='characters/', null=True, blank=True)

    def __str__(self):
        return self.name


# h = Character(name="Hulk", description="angry",
#               powers="gamma", affiliation="avengers", image="null")
