from django.contrib import admin

from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug',
        'jpublish','status',
        'category_to_string',
    )

    list_filter = (
        'publish', 'status'
    )
    search_fields = (
        'title', 'description'
    )
    prepopulated_fields = {
        'slug': ('title',)
    }

    ordering = ['status', 'publish']

    def category_to_string(self, obj):
       return ", ".join([category.title for category in obj.category_published()])
    category_to_string.short_description = 'دسته بندی'

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'title', 'slug',
        'status', 'parent'
    )

    list_filter = (
        ['status',]
    )
    search_fields = (
        'title', 'slug',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }



admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)