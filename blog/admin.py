from django.contrib import admin
from .models import Post,Tag,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','category','author']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)