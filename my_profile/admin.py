from django.contrib import admin
from my_profile.models import Post, Tag, Comment

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)