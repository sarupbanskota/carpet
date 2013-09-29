from django.contrib import admin
from votein_server.models import Vote, Article, Opinion

class OpinionInline(admin.StackedInline):
    model = Opinion
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    inlines = [OpinionInline]
    list_display = ('user', 'articleName', 'articleLink', 'articleCreationTime', 'articleLastEditTime')

admin.site.register(Article, ArticleAdmin)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'opinion', 'voteType')
    
admin.site.register(Vote, VoteAdmin)
