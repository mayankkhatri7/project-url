from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):
	list_display=('title','date','url')

admin.site.register(Bookmark,BookmarkAdmin)