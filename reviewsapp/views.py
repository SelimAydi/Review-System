from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import Reviews
# Create your views here.

def index(request):
	errors = []
	if request.method == "POST":
		form = forms.ReviewForm(request.POST)
		print(request.POST)
		
		if not request.POST.get('review'):
			print("review empty")
			errors.append("Review veld is leeg.")
			return render(request, 'index.html', {'form' : form, 'errors': errors})
		elif not request.POST.get('user_name') and request.POST.get('anon') != 'on':
			print("username empty")
			errors.append("U heeft uw naam nog niet ingevuld.")
			return render(request, 'index.html', {'form' : form, 'errors': errors})
		elif int(request.POST.get("rating")) < 1:
			print("rating empty")
			errors.append("Uw heeft nog niet beoordeeld.")
			return render(request, 'index.html', {'form' : form, 'errors': errors})
		
		if form.is_valid():
			print("is valid")
			
			if request.POST.get('anon') == 'on':
				print("anonymous")
				reviewrecord = Reviews(user_name='anoniem', rating=request.POST['rating'], review=request.POST['review'])
			else:
				reviewrecord = Reviews(user_name=request.POST['user_name'], rating=request.POST['rating'], review=request.POST['review'])
			reviewrecord.save()
			return render(request, 'succes.html', {'form' : form, 'errors': errors})
			
		if request.POST.get('anon') == 'on':
			print("true")
	else:
		print(request.method)

	form = forms.ReviewForm()
	
	return render(request, 'index.html', {'form' : form})

def reviewview(request):
	return render(request, 'reviews.html', {'rows': Reviews.objects.all().order_by('-id')})