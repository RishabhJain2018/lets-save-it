from django.forms import ModelForm
from conserve.models import *

class UserForm(ModelForm):
	class Meta:
		model= UserData
		fields='__all__'


class BillForm(ModelForm):
	class Meta:
		model = BillData
		fields = '__all__'