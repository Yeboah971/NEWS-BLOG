from django.contrib import admin
from .models import Blog_Post, comment

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
 
admin.site.register(Blog_Post, BlogPostAdmin)
admin.site.register(comment)




