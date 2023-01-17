from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tour(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    slug = models.SlugField(auto_created=True)
    duration = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    placed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "旅遊行程"
        verbose_name = "旅遊行程"

    def __str__(self):
        return self.title
