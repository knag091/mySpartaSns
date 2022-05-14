from django.contrib import admin
from .models import TweetModel, TweetComment

admin.site.register(TweetModel)
admin.site.register(TweetComment)