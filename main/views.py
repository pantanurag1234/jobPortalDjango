from django.shortcuts import render

#by me
from django.http import HttpResponse 
from .models import organisations, registration
from .form import landingForm
from django.shortcuts import *
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def empty(request):
    return render(request, 'mainTemplates/pages/empty.html')

def login(request):
    # return HttpResponse('Login Page')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:

            login(request, user)

            return redirect("/landing/")

        else:
            messages.info(request, 'Invalid Credential!!')
            return redirect("login")

    else:
        return render(request, 'mainTemplates/pages/login.html')

def register(request):
    # ----------------------------------------------------------------------
    # # return HttpResponse('Register Page')
    # reg_Form = regForm()
    
    # if request.method == 'POST':
    #     name = request.post.get('name')
    #     email = request.post.get('email')
    #     password = request.post.get('password')
    #     confirm_password = request.post.get('confirm_password')
    #     if regg_Form.is_valid():
    #         regg_Form.save()
    #         return redirect('/login')
        

    # context = {'reg_Form':reg_Form}
    # return render(request, 'mainTemplates/pages/register.html',context)
    # ----------------------------------------------------------------------
    if request.method == 'POST':
        varUsername = request.POST.get('username')
        varEmail = request.POST.get('email')
        varPassword = request.POST.get('password')
        varConfirm_password = request.POST.get('confirm_password')

        # Check if the passwords match
        if varPassword != varConfirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # Check if the username is already taken
        if User.objects.filter(username=varUsername).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')

        # Check if the email is already registered
        if User.objects.filter(email=varEmail).exists():
            messages.error(request, 'Email is already registered')
            return redirect('register')

        # Create a new user account
        user = User.objects.create_user(
            username=varUsername,
            email=varEmail,
            password=varPassword
        )
        messages.success(request, 'Account created successfully! You can now login.')
        return redirect('register')

    return render(request, 'mainTemplates/pages/register.html')


def landing(request):
    orgForm = landingForm()
    # return HttpResponse('Landing Page')
    #inside post is name given to input tag in landing.html
    # var_orgName = request.POST.get('orgName',False); 
    # var_orgPosition = request.POST.get('orgPosition',False);
    # var_orgPackage = request.POST.get('orgPackage',False);
    # var_orgExperience = request.POST.get('orgExperience',False);
    # var_orgVacancies = request.POST('');

    if request.method == 'POST':
        landing_Form = landingForm(request.POST)
        if landing_Form.is_valid():
            # insertingOrganisation = organisations(name=var_orgName, position=var_orgPosition, package_in_LPA=var_orgPackage, experience_in_yrs=var_orgExperience);
            # insertingOrganisation.save();
            landing_Form.save()
            return redirect('/landing')
        else:
            # return HttpResponse("Can't leave fields empty")
            return redirect('/login')
    else:
        organisationsTableData = organisations.objects.all()
    context = {
        'orgForm': orgForm,
        'organisationsTableData': organisationsTableData,
        }

    return render(request, 'mainTemplates/pages/landing.html', context)

    # organisationsTableData = organisations.objects.all()

    # return render(request, 'mainTemplates/pages/landing.html',{'organisationsTableData': organisationsTableData})

# @login_required
# def landing(request):
#     landing(request)
#     return redirect("login")

def apply(request):
    # return HttpResponse('Apply Page')
    return render(request, 'mainTemplates/pages/apply.html')


