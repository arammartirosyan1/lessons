from django.db import models


class Languages(models.Model):
    language_name = models.CharField(max_length=50)
    pube_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.language_name


class Types(models.Model):
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

