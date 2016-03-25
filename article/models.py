from django.db import models

class Articles(models.Model):

    title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)
    bodytext = models.TextField(blank=True)
    image = models.CharField(max_length=200, blank=True)
    image_small = models.CharField(max_length=200, blank=True)
    publication_date = models.DateField(null=True, db_index=True)

