from django.contrib import admin
from embed_video.admin  import  AdminVideoMixin
from .models  import  newProduct , pages, contectusemail
#Register your models here.

class  tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(newProduct, tutorialAdmin)
admin.site.register(contectusemail)
admin.site.register(pages)
class pagesadmin(admin.ModelAdmin):
	class Media:
		ja = ('tinyinject.js')



