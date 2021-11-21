from django.db import models
#Define Shahid-Model
class ShahidModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='shahids/')
    born_date = models.DateTimeField()
    shahadat_date = models.DateTimeField()
    class Meta:
        verbose_name = 'شهید'
        verbose_name_plural = 'شهدا'

    def __str__(self):
        return self.name
    @property
    def imageUrl(self):
        return self.image.path
