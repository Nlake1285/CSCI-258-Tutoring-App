from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class TutoringHour(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    
    tutor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_tutor': True}
    )
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100, default="CS Fishbowl")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('tutor', 'day_of_week', 'start_time')
        ordering = ['day_of_week', 'start_time']
    
    def __str__(self):
        return f"{self.tutor.username} - {self.get_day_of_week_display()} {self.start_time}-{self.end_time}"
    
    def get_absolute_url(self):
        return reverse("tutor_detail", kwargs={"pk": self.tutor.pk})