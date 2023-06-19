from django.db import models
from django.utils import timezone


class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    data_created = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name_plural = "Entries"
