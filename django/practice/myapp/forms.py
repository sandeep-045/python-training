from django import forms 
from myapp import models


class UserForm(forms.ModelForm):
	
	class Meta:
		model = models.User
		fields = ('name','email')


