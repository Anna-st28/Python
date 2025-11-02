from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField('Кнопка')

    def __str__(self):
        return self.title
