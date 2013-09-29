# Create your views here.
from votein_server.models import *
from django.views.generic import DetailView, ListView, TemplateView
from django.template import Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

class ErrorView(TemplateView):
    def get_context_data(self):
        return render_to_response('errorpage.html')

def ArticleReadView(request, embedcode):
    try:
        article = getArticle(embedcode)
        return HttpResponseRedirect('/carpet/renderarticle/%s/' % article.embed_code)
    except:
        return HttpResponseRedirect('/error/')

def AddVote(self, vote):
    if vote.voteType == Vote.VOTE_CHOICES.Up:
        self.opinionVotes.upVotes.add(vote) 
    elif vote.voteType == Vote.VOTE_CHOICES.Down:
        self.opinionVotes.downVotes.add(vote)
    self.save()



def getArticle(embedcode):
    try:
        art = Article.objects.get(embed_code=embedcode)
    except ObjectDoesNotExist:
        return "Article does not exist"

def getArticleUpVotes(obj):
    try:
        art = Article.objects.get(obj = obj)
        return art.articleVotes.upVotes.count()
    except ObjectDoesNotExist:
        print "Article does not exist"

def getArticleDownVotes(obj):
    try:
        art = Article.objects.get(obj = obj)
        return art.articleVotes.downVotes.count()
    except ObjectDoesNotExist:
        print "Article does not exist"

def getOpinionUpVotes(obj):
    try:
        op = Opinion.objects.get(obj = obj)
        return op.opinionVotes.upVotes.count()
    except ObjectDoesNotExist:
        print "Opinion does not exist"

def getOpinionDownVotes(obj):
    try:
        op = Opinion.objects.get(obj = obj)
        return op.opinionVotes.downVotes.count()
    except ObjectDoesNotExist:
        print "Opinion does not exist"

