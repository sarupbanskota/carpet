from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView
from votein_server.models import *
from votein_server.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carpet.views.home', name='home'),
    # url(r'^carpet/', include('carpet.foo.urls')),
    url(r'^renderarticle/(?P<embedcode>\d+)/$', DetailView.as_view(
		template_name='article-read.html',
		model=Article,
		context_object_name='article'
	)),

	url(r'^article/(?P<embedcode>\d+)/$', ArticleReadView),

    url(r'^error/$', ErrorView.as_view(
		template_name='errorpage.html'
	)),

    #url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	
	#url(r'signup/$', signup),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
