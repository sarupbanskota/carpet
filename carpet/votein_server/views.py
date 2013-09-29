# Create your views here.
from votein_server.models import *
from django.views.generic import DetailView, ListView, TemplateView
from django.template import Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

class ErrorView(TemplateView):
	def get_context_data(self):
		return RequestContext(self.request)

def ArticleReadView(request, embedcode):
	try:
		article = getArticle(embedcode)
		return HttpResponseRedirect('/carpet/renderarticle/%s/' % article.embed_code)
	except:
		return HttpResponseRedirect('/error/')