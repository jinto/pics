from django.db import models

# Create your models here.

class Photo(models.Model):
    photo_id = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=1024, unique=True)
    scaned_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _url(self):
        "Returns the person's full name."
        return '/%s' % (self.path)
    url = property(_url)
