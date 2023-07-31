from django.db import models

# Create your models here.
class results(models.Model):
    seat_no = models.IntegerField()
    totalDegree = models.IntegerField()
    name = models.CharField(max_length=3200)
    state = models.CharField(max_length=3200)

    def serialize(self):
        return {
            'name' : self.name,
            'seatNo' : self.seat_no,
            'degree' : self.totalDegree,
            'state' : self.state
        }