from django.contrib import admin
from . import models

# to appear on admin page
admin.site.register(models.Post)