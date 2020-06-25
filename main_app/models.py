from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


COACHES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evining')
)

class Coach(models.Model):
  name = models.CharField(max_length=50)
  position = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('coaches_detail', kwargs={'pk': self.id})

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    country = models.TextField(max_length=50)
    age         = models.IntegerField()
    coaches = models.ManyToManyField(Coach)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})

class Training(models.Model):
    date = models.DateField('training date')
    coach = models.CharField(
        max_length=1,
        choices=COACHES,
        default=COACHES[0][0]
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_coach_display()} on {self.date}"
class Meta:
    ordering = ['-date']

