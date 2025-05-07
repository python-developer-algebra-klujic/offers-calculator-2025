from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Male, Female, Other
