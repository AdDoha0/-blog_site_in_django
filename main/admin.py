from django.contrib import admin

from .models import Post, Category


admin.site.index_title = "Хадисы"
admin.site.site_header = "Панель администрирования"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ["title", "slug", "content", "is_published", "cat", "is_featured"]
    prepopulated_fields = {"slug": ("title", )}
    list_per_page = 5
    list_display = ('id', 'title', 'time_create', 'is_published', "cat", "is_featured")
    list_editable = ('is_published', "is_featured")
    list_filter = ('is_published', 'is_featured')




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name", )}




