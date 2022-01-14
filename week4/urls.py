from django.urls import path
from .views import soft_delete_profile,recover_profile

urlpatterns=[
	path('deleted/<int:pk>/',soft_delete_profile,name='soft_delete_profile'),
	path('recover/<int:pk>/',recover_profile,name='recover_profile'),
]