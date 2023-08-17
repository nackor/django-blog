from django.contrib import admin
from blogging.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

class CategoryInLine(admin.TabularInline):
    pass
class PostAdmin(admin.ModelAdmin):
    pass



admin.site.register(Post)
admin.site.register(Category, CategoryAdmin) 