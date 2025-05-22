from django.contrib import admin

# Register your models here.
from .models import Profile, Project, Skill, ContactMessage
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(ContactMessage)