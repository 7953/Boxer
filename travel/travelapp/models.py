from django.db import models


class boxer(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name
  