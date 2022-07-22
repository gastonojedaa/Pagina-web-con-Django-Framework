from django.contrib import admin
from .models import category,post
# Register your models here.


class adminCategory(admin.ModelAdmin):
    readonly_fields=("created","updated")
    
class adminPost(admin.ModelAdmin):
    readonly_fields=("created","updated")


admin.site.register(category,adminCategory)
admin.site.register(post,adminPost)
