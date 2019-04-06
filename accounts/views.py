from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):
	if request.method=='POST':
		if request.POST['password1'] == request.POST['password2']:
			# check if the username has already been taken
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error' : "Username has already been taken"})
			except User.DoesNotExist:
				user = User.objects.create_user(
					username=request.POST['username'], 
					password=request.POST['password1'])
				# logging in as the user who signed up, can't access admin page now
				login(request, user) 
				return render(request, 'accounts/signup.html', {'error' : "New User created"})
		else:
			return render(request, 'accounts/signup.html', {'error' : "Paswords didn't match"})
	else:
		return render(request, 'accounts/signup.html')

def login_view(request):
	if request.method=='POST':
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return render(request, 'accounts/login.html', {'error' : 'Logged in Successfully'})
		else:
			return render(request, 'accounts/login.html', {'error' : "Account does not exist OR Username and Password didn't match"})
	else:
		return render(request, 'accounts/login.html')
