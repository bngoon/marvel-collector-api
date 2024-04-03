from django.db import models

# Create your models here.
RATINGS = (
    ('N', 'New'),
    ('F', 'Fair'),
    ('U', 'Used'),
)


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    powers = models.TextField(max_length=250)
    affiliation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='characters/', null=True, blank=True)

    def __str__(self):
        return self.name


class Condition(models.Model):
    date = models.DateField('Date Collected')
    rating = models.CharField(
        max_length=1, choices=RATINGS, default=RATINGS[0][0])
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
