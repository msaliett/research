from django.contrib import admin

from .models import Project
from .models import Investigator
from .models import Assignment

# Register your models here.
admin.site.register(Project)
admin.site.register(Investigator)
admin.site.register(Assignment)