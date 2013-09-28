from django.db import models

class Vote(models.Model):
    voter_ID = models.CharField(max_length=50)      #can be external like Facebook ID
