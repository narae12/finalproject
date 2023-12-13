from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리할 수 있도록 등록
from .models import Photo
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    raw_id_fields = ['author']
    list_filter = ['created','updated','author']
    search_fields = ['text','created','author__username']
    ordering = ['-updated','-created']

admin.site.register(Photo,PhotoAdmin)