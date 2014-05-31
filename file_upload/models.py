from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class FileUpload(models.Model):
    user = models.ForeignKey(User,related_name="user")
    file = models.FileField(upload_to='uploaded_files')
    name = models.CharField(max_length=100,null=True,blank=True)

    def __unicode__(self):
        return self.name
