from django.db import models


class Picture(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')

    @property
    def url(self):
        return '/' + self.image.url
