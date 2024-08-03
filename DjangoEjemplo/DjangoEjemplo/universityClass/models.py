from django.db import models

# Create your models here.
class UniversityClass(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=5, unique=True)
    department =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} {self.name}"

    class Meta:
        verbose_name = "Clase Universitaria"
        verbose_name_plural = "Clases Universitarias"
        ordering = ['-name']