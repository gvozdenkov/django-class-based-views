from django.db import models

# Create your models here.

class Message(models.Model):
    username = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self) -> str:
        return f"username: {self.username}, msg: '{self.message[:20]}'"
