from django.db import models


class Post(models.Model):
    id = models.AutoField(unique=True, blank=False, primary_key=True)
    title = models.CharField(max_length=128, null=False)
    description = models.TextField(max_length=500, null=True)

    def __unicode__(self):
        return self.title
