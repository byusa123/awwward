from django.contrib import admin
from .models import Profile, Project, Location, tags, Comment, Ratings


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Comment)
admin.site.register(Ratings)
