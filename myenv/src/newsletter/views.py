from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm
from .forms import ContactForm
# Create your views here.

def home(request):
	title = "Welcome"
	#if request.user.is_authenticated():
	#	title = "My Title %s" %(request.user)
	
	form = SignUpForm(request.POST or None)
	context = {
	"title": title,
	"form": form,
	}
	if form.is_valid():
		# form.save()

		instance = form.save(commit = False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		# print instance
		context = {
		"title": "Thank you",
		}
	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	form_email = form.cleaned_data.get("email")
	form_message = form.cleaned_data.get("message")
	form_name = form.cleaned_data.get("full_name")
	context = {
		"form": form,
	}
	subject = 'contact form' 
	from_email = settings.EMAIL_HOST_USER
	to_email = from_email
	# send_mail(
 #    subject,
 #    'Here is the message.',
 #    from_email,
 #    [to_email],
 #    fail_silently=False,
	# )
	return render(request, "forms.html", context)