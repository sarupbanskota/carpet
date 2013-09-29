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
from django.contrib.auth.models import User

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

def home(request):
    return render(request, "votein_server/index.html")

def about(request):
    return render(request, "votein_server/about.html")

def contact(request):
    return render(request, "votein_server/contact.html")

def login_user(request):
    if request.user.is_authenticated():
        return redirect("app")
    else:
        if len(request.POST) == 0:
            return render(request, "votein_server/login.html")
        if request.POST['username'] == "":
            return render(request, "votein_server/login.html", {"error_message": "Please input username!"})
        elif request.POST['password'] == '':
            return render(request, "votein_server/login.html", {"error_message": "Please input password!"})
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return redirect("app")
                else:
                    return HttpResponse("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                return render(request, "votein_server/login.html", {"error_message": "The username or password you entered is incorrect."})

def signup(request):
    if request.user.is_authenticated():
        return redirect("app")
    else:
        if len(request.POST) == 0:
            return render(request, "votein_server/signup.html")
        if request.POST['username'] == "":
            return render(request, "votein_server/singup.html", {"error_message": "Please input username!"})
        elif request.POST['password'] == '':
            return render(request, "votein_server/signup.html", {"error_message": "Please input password!"})
        elif request.POST['email'] == '':
            return render(request, "votein_server/signup.html", {"error_message": "Please input email address!"})
        else:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.save()
            return render(request, "votein_server/login.html")

def app(request):
    return render(request, "votein_server/app.html")
