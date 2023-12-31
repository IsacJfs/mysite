from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "status", "created_on"]
    list_filter = ["status", "created_on"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)