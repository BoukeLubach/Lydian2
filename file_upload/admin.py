from django.contrib import admin
from .models import Tagmodel, Datafile, Batch

admin.site.register(Tagmodel)
admin.site.register(Datafile)
admin.site.register(Batch)
# Register your models here.
