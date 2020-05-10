from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 80)
    desc = models.CharField(max_length = 150)
    date = models.DateField()
    author = models.CharField(max_length = 40)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title