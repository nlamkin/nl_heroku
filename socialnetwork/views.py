from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import transaction

from socialnetwork.models import *


@login_required
def welcome(request):
    return render(request, 'socialnetwork/homeLogin.html', {})

def stream(request):
    posts = Post.objects.all()
    return render(request, 'socialnetwork/stream.html', {})

def registerNewUser(request):
    context = {}

    if request.method == 'GET':
        return render(request, 'socialnetwork/register.html', context)
    
    errors = []
    context['errors'] = errors

    # Check that a username was submitted
    if not 'username' in request.POST or not request.POST['username']:
    	errors.append('Username is required.')
    else:
        # Save the username to repopulate form if there are errors
        context['username'] = request.POST['username']
        # Check that the chosen username is available
        if len(User.objects.filter(username = request.POST['username'])) > 0:
            errors.append('Username is already taken.')
        
    # Check that a first name was submitted    
    if not 'first_name' in request.POST or not request.POST['first_name']:
    	errors.append('Please enter your first name')
    else:
        # Save the name to repopulate form if there are errors
        context['first_name'] = request.POST['first_name']
        
    # Check that a last name was submitted    
    if not 'last_name' in request.POST or not request.POST['last_name']:
    	errors.append('Please enter your last name')
    else:
        # Save the name to repopulate form if there are errors
        context['last_name'] = request.POST['last_name']
    
    # Make sure a password was entered in both cases
    if not 'password1' in request.POST or not request.POST['password1']:
        errors.append('Password is required.')
    if not 'password2' in request.POST or not request.POST['password2']:
        errors.append('Confirm password is required.')
    
    # Check that passwords match
    if 'password1' in request.POST and 'password2' in request.POST \
            and request.POST['password1'] and request.POST['password2'] \
            and request.POST['password1'] != request.POST['password2']:
        errors.append('Passwords did not match.')

    if errors:
        return render(request, 'socialnetwork/register.html', context)
        
    new_user = User.objects.create_user(username=request.POST['username'], \
                                        password=request.POST['password1'])
    new_user.save()
    
    new_user = authenticate(username=request.POST['username'], \
                            password=request.POST['password1'])
    login(new_user)
    return redirect('/stream/')