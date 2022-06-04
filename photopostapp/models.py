from django.db import models


# Create your models here.
class PhotoUpload(models.Model):
    image = models.ImageField(upload_to="images", null=True)
    caption = models.CharField(max_length=200)
    author_name = models.CharField(max_length=20)

    def __str__(self):
        return self.author_name
