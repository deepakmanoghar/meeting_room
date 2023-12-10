
from django.db import models
from django.utils import timezone

class MeetingRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def is_conflicting(self):
        conflicting_bookings = Booking.objects.filter(
            room=self.room,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )
        return conflicting_bookings.exists()