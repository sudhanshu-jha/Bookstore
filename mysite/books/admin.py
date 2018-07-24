from django.contrib import admin
from .models import Book

app = apps.get_app_config('mysite.books')
for model_name, model in app.models.items():
    admin.site.register(model)

