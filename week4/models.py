from django.db import models

# Create your models here.

class Profile(models.Model):
	class GenderChoices(models.TextChoices):
		MALE = "M","Male"
		FEMALE = "F","Female"
		OTHER = "O","Other"


	deleted = models.BooleanField(default=False)
	name = models.CharField(max_length=100)
	gender = models.CharField(max_length=10,choices=GenderChoices.choices)
	dob = models.DateField()
	nationality = models.CharField(max_length=50)
	address = models.CharField(max_length=15)

	def __str__(self):
		return str(self.name)


class ProfileProxy(Profile):
	class Meta:
		verbose_name='Profile Trash'
		verbose_name_plural='Profiles Trash'
		proxy=True