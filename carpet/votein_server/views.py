# Create your views here.
from votein_server.models import Article, Opinion, Vote
from django.views.generic import DetailView, ListView, TemplateView
from django.template import Context, RequestContext, loader
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

def home(request):
    return render(request, "votein_server/index.html")

def about(request):
    return render(request, "votein_server/about.html")

def contact(request):
    return render(request, "votein_server/contact.html")

def login(request):
    return render(request, "votein_server/login.html")

def signup(request):
    return render(request, "votein_server/signup.html")
