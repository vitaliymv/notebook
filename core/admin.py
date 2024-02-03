from django.contrib import admin
from core.models import models_list, Category

# Register your models here.

for model in models_list:
    admin.site.register(model)

