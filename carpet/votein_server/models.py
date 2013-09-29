from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User)
    articleName = models.CharField(blank=True, max_length=140)
    articleLink = models.CharField(max_length = 200)
    articleCreationTime = models.DateTimeField(auto_now_add = True)
    articleLastEditTime = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        return '{0.user}, {0.articleName}, {0.articleLink}, {0.articleCreationTime}, {0.articleLastEditTime}'.format(self)

class Opinion(models.Model):
    article = models.ForeignKey(Article)
    opinionText = models.TextField(max_length=1000)
    opinionCreationTime = models.DateTimeField(auto_now_add = True)
    opinionLastEditTime = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        return '{0.article}, {0.opinionText}, {0.opinionCreationTime}, {0.opinionLastEditTime}'.format(self)

class Vote(models.Model):
    DOWN = 'D'
    UP = 'U'
    VOTE_CHOICES = (
        (DOWN, 'Down'),
        (UP, 'Up'),
    )
    user = models.ForeignKey(User)
    opinion = models.ForeignKey(Opinion)
    voteType = models.CharField(max_length=1, choices=VOTE_CHOICES)
    def __unicode__(self):
        return '{0.opinion}, {0.user}, {0.voteType}'.format(self)
