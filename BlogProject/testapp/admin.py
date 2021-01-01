from django.contrib import admin
from testapp.models import Post
# Register your models here.
class PostAmdin(admin.ModelAdmin):
    list_display=['title','description','created_at','user','status','slug']
    list_filter=('user','status','created_at')
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','description')



admin.site.register(Post,PostAmdin)
