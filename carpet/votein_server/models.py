from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class Vote(models.Model):
	submitter = models.CharField(max_length=50)		#can be external like Facebook ID
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

# Used by Article class
class Image(models.Model):
	submitter = models.CharField(max_length=50)
	imageURL = models.URLField();					#Do we need images as opinions, like an artist's work etc?
	def __unicode__(self):							#Also, Consider changing this to FileField
		return self.imageURL

###########################################################################
######					Main Class Models  								###
###########################################################################

# Used by Article class
class Comment(models.Model):
	commentText = models.CharField(max_length=1000)
	commentVotes = models.ManyToManyField(Vote)
	submitter = models.CharField(max_length=50)
	def __unicode__(self):
		return self.commentText
	def AddVote(self, vote):
		if vote.voteType == Vote.VOTE_CHOICES.Up:
			self.commentVotes.upVotes.add(vote) 
		elif vote.voteType == Vote.VOTE_CHOICES.Down:
			self.commentVotes.downVotes.add(vote)
		self.save()

# Used by the Article class
class Opinion(models.Model):
	opinionText = models.CharField(max_length=1000)
	submitter = models.CharField(max_length=50)
	opinionComment = models.ManyToManyField(Comment)
	opinionVotes = models.ManyToManyField(Vote)
	def __unicode__(self):
		return self.opinionText
	def addComment(self, comment):
		self.comment.add(comment)
	def AddVote(self, vote):
		if vote.voteType == Vote.VOTE_CHOICES.Up:
			self.opinionVotes.upVotes.add(vote) 
		elif vote.voteType == Vote.VOTE_CHOICES.Down:
			self.opinionVotes.downVotes.add(vote)
		self.save()

class Article(models.Model):
	articleName = models.CharField(max_length=100)
	submitter = models.CharField(max_length=50)
	#articeOpinion = ManyToManyField(Opinion)
	#articleComments = ManyToManyField(Comment)
	articleVotes = ManytoManyField(Vote)
	def __unicode__(self):
		return self.name
	def addComment(self, comment):
		self.comment.add(comment)
	def AddVote(self, vote):
		if vote.voteType == Vote.VOTE_CHOICES.Up:
			self.articleVotes.upVotes.add(vote) 
		elif vote.voteType == Vote.VOTE_CHOICES.Down:
			self.articleVotes.downVotes.add(vote)
		self.save()
