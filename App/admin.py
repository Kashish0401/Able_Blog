from django.contrib import admin

# Register your models here.
from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
  list_display = ('title',  'date_created')
  search_fields = ['title', 'content']
  
admin.site.register(PostModel, PostModelAdmin)