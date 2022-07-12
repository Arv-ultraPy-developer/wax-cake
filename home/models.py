from django.db import models

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__ (self):
        return self.name




