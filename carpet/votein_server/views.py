# Create your views here.
from votein_server.models import *
from django.views.generic import DetailView, ListView, TemplateView
from django.template import Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

class ErrorView(TemplateView):
    def get_context_data(self):
        return render_to_response('errorpage.html')

def ArticleReadView(request, articleLink):
    try:
        article = getArticle(articleLink)
        return HttpResponseRedirect('/renderarticle/%s/' % article.articleLink)
    except:
        #return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/error/')

def AddVote(self, vote):
    if vote.voteType == Vote.VOTE_CHOICES.Up:
        self.opinionVotes.upVotes.add(vote) 
    elif vote.voteType == Vote.VOTE_CHOICES.Down:
        self.opinionVotes.downVotes.add(vote)
    self.save()
