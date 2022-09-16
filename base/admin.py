from django.contrib import admin
from .models import Complaint, Comment, ProgressBar
# Register your models here.
from .models import User
admin.site.register(User)
admin.site.register(Complaint)
admin.site.register(Comment)

admin.site.register(ProgressBar)