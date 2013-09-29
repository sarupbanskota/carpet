from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User)
    articleName = models.CharField(max_length=100)
    submitter = models.CharField(max_length=50)
    articleLink = models.URLField(blank=True, max_length = 200)
    embedCode = models.FloatField(max_length=50)
    # articleComments = models.ManyToManyField(Comment)
    articleLastEdit = models.DateTimeField(auto_now_add = True)
    #articleVotes = models.ManytoManyField(Vote)
    def __unicode__(self):
        return self.articleName
    def AddVote(self, vote):
        if vote.voteType == Vote.VOTE_CHOICES.Up:
            self.articleVotes.upVotes.add(vote) 
        elif vote.voteType == Vote.VOTE_CHOICES.Down:
            self.articleVotes.downVotes.add(vote)
        self.save()

# Used by the Article class
class Opinion(models.Model):
    articleID = models.ForeignKey(Article)
    opinionText = models.CharField(max_length=1000)
    submitter = models.CharField(max_length=50)
    # opinionComment = models.ManyToManyField(Comment)
    def __unicode__(self):
        return self.opinionText

class Vote(models.Model):
    opinionID = models.ForeignKey(Opinion)
    user = models.ForeignKey(User)      #can be external like Facebook ID?
    DOWN = 'Dw'
    UP = 'Up'
    VOTE_CHOICES = (
        (DOWN, 'Down'),
        (UP, 'Up'),
    )
    voteType = models.CharField(max_length=2, choices=VOTE_CHOICES, default=UP)
    def __unicode__(self):
        return self.voteType in (self.UP, self.DOWN)


# Used by Article class
# class Image(models.Model):
#   submitter = models.CharField(max_length=50)
#   imageURL = models.URLField();                   #Do we need images as opinions, like an artist's work etc?
#   def __unicode__(self):                          #Also, Consider changing this to FileField
#       return self.imageURL

# Used by Article class
# class Comment(models.Model):
#   commentText = models.CharField(max_length=1000)
#   commentVotes = models.ManyToManyField(Vote)
#   submitter = models.CharField(max_length=50)
#   def __unicode__(self):
#       return self.commentText
#   def AddVote(self, vote):
#       if vote.voteType == Vote.VOTE_CHOICES.Up:
#           self.commentVotes.upVotes.add(vote) 
#       elif vote.voteType == Vote.VOTE_CHOICES.Down:
#           self.commentVotes.downVotes.add(vote)
#       self.save()

# def getCommentUpVotes(obj):
#   try:
#       cmt = Comment.objects.get(obj = obj)
#       return cmt.commentVotes.upVotes.count()
#   except ObjectDoesNotExist:
#       print "Comment does not exist"

# def getCommentDownVotes(obj):
#   try:
#       cmt = Comment.objects.get(obj = obj)
#       return cmt.commentVotes.downVotes.count()
#   except ObjectDoesNotExist:
#       print "Comment does not exist"
