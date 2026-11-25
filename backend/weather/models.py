from django.db import models
from django.utils import timezone


class WeatherData(models.Model):
    city = models.CharField(max_length=120, db_index=True)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        ordering = ["-timestamp", "-id"]
        indexes = [
            models.Index(fields=["city", "-timestamp"]),
        ]

    def __str__(self) -> str:
        return f"{self.city} ({self.temperature}°C) @ {self.timestamp:%Y-%m-%d %H:%M}"