from django.db import models

class CapturedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem {self.id} - {self.timestamp}"