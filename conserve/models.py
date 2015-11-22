from django.db import models
from django.forms import ModelForm

# Create your models here.

class UserData(models.Model):
	'''models for users profile '''
	name=models.CharField(max_length=200)
	father_name=models.CharField(max_length=200,null=True)
	address=models.CharField(max_length=200)
	mob=models.IntegerField(blank=False)
	email=models.EmailField()
	bill_no=models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.email

class BillData(models.Model):
	prescribed_unit=models.IntegerField()
	alert_unit=models.IntegerField()
	current_unit=models.IntegerField()

	def __unicode__(self):
		return alert_unit