from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        errors = []
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user != None:
            login(request, user)
            
            return redirect('main')
        else:
            errors.append('User does not exists!')

        return render(request, 'login.html', {'errors': errors})


class SignInView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        errors = []

        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password'] 

        if len(password) < 8:
            errors.append('The password cannot be less than 8 characters!')

            return render(request, 'signin.html', {'errors': errors})

        if repeat_password == password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                return redirect('login')
            except IntegrityError:
                errors.append('This user exists!')

        else:
            errors.append('Repeat password is incorrect!')

        return render(request, 'signin.html', {'errors': errors})


class LogoutView(View):
    def get(self, request):
        logout(request)

        return redirect('signin')







