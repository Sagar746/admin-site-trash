from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Profile

# Create your views here.


def soft_delete_profile(request,pk):
	profile=Profile.objects.get(id=pk)
	if not request.user.is_superuser:
		raise Http404('YOU ARE NOT ALLOWED')
	profile.deleted=True
	profile.save()
	# return HttpResponse('Deleted has been set to True')
	return HttpResponseRedirect('http://127.0.0.1:8000/admin/week4/profile/')


def recover_profile(request,pk):
	profile=Profile.objects.get(id=pk)
	profile.deleted=False
	profile.save()
	# return HttpResponse('Deleted has been set to True')
	return HttpResponseRedirect('http://127.0.0.1:8000/admin/week4/profileproxy/')