from django.db import models
from django.utils import timezone


class WeatherData(models.Model):
    city = models.CharField(max_length=120, db_index=True)
    temperature = models.FloatField(help_text="Temperatura en grados Celsius")
    humidity = models.FloatField(help_text="Humedad relativa en porcentaje")
    wind_speed = models.FloatField(help_text="Velocidad del viento en m/s o km/h")
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        ordering = ["-timestamp", "-id"]
        indexes = [
            models.Index(fields=["city", "-timestamp"]),
        ]

    def __str__(self) -> str:
        return f"{self.city} ({self.temperature}°C) @ {self.timestamp:%Y-%m-%d %H:%M}"