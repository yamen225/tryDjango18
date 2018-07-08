from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email', 'full_name' ]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not "edu" in email:
			raise forms.ValidationError("Please use a .edu email")
		return email