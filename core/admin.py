from django.contrib import admin
from .models import category, blog, sociallinks, comment
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','author','status','category','is_featured')
    search_fields = ('id','title','status','category__category_name')
    list_editable = ('is_featured',)


admin.site.register(category)
admin.site.register(blog,BlogAdmin)
admin.site.register(sociallinks)
admin.site.register(comment)
