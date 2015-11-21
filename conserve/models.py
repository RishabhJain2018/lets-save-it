from django.db import models

# Create your models here.

class UserData(models.Model):
	name=models.CharField(max_length=200,null=False,blank=False)
	father_name=models.CharField(max_length=200,null=False,blank=False)
	dob=models.IntegerField()
	address=models.CharField(max_length=200,blank=False)
	mob=models.IntegerField(max_length=10,blank=False,default=0)


	


