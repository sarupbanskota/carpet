from django.db import models

class Vote(models.Model):
    voter_ID = models.CharField(max_length=50)      #can be external like Facebook ID
    DOWN = 'Dw'
    UP = 'Up'
    VOTE_CHOICES = (
        (DOWN, 'Down'),
        (UP, 'Up'),
    )
    voteType = models.CharField(max_length=2,
                                      choices=VOTE_CHOICES,
                                      default=UP)
    def __unicode__(self):
        return self.voteType in (self.UP, self.DOWN)
