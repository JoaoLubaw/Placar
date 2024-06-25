from django.db import models

class Ponto(models.Model):
    ORIGEM_CHOICES = [
        ('joao', 'João'),
        ('benja', 'Benja'),
    ]

    title = models.CharField(max_length=200)
    ID = models.AutoField(primary_key=True)
    origem = models.CharField(max_length=5, choices=ORIGEM_CHOICES, default='joao')

    def __str__(self):
        return f"{self.title} ({self.get_origem_display()})"
