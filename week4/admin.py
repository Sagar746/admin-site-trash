from django.contrib import admin
from django.urls import reverse
from .models import Profile,ProfileProxy
from django.utils.html import format_html

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display=['name','gender','dob','nationality','address','delete_action']
	list_editable=('gender',)

	actions=['change_all_to_female']

	def delete_action(self,obj):
		return format_html(
			"<a class='button' style='background-color:maroon;' href='{}'>Delete</a>",
			reverse('soft_delete_profile',args=[obj.pk]),
		)
	delete_action.short_description='delete'

	def change_all_to_female(self,request,queryset):
		queryset.update(gender='F')


	def get_queryset(self,*args,**kwargs):
		return super().get_queryset(*args,**kwargs).filter(deleted=False)


@admin.register(ProfileProxy)
class ProfileTrashAdmin(admin.ModelAdmin):
	list_display=['name','gender','dob','nationality','address','recover_action']
	list_editable=('gender',)

	def recover_action(self,obj):
		return format_html(
			"<a class='button' style='background-color:green;' href='{}'>Recover</a>",
			reverse('recover_profile',args=[obj.pk]),
		)
	recover_action.short_description='recover'


	def get_queryset(self,*args,**kwargs):
		return super().get_queryset(*args,**kwargs).filter(deleted=True)