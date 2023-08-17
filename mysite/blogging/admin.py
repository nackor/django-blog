from django.contrib import admin
from blogging.models import Post, Category

# and a new admin registration
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts')


admin.site.register(Category)   