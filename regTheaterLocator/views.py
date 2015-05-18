from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import transaction

from datetime import datetime

from regTheaterLocator.forms import *
from regTheaterLocator.models import *


# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate

def index(request):
   return render(request, 'regTheaterLocator/index.html', {})

def results(request):

   return render(request, 'regTheaterLocator/index.html', {})

def generateTheaterContext(theater):
    context = {}
    context['theaterName'] = theater.name
    context['address'] = theater.address
#    context['boxOfficePhone']=theater._meta.get_field('phone')
    context['city'] = theater.city
    context['state']=theater.state
    context['zip_code'] = theater.zip_code
    productions = Production.objects.filter(theater=theater)
    context['productions'] = productions
    return context

@login_required    
def theaterSearch(request):
    if not 'theaterName' in request.GET and not 'city' in request.GET:
        return render(request, 'regTheaterLocator/search.html', {})
    name = request.GET.get('theaterName')
    city = request.GET.get('city')
    if name:
        if city:
            objects = Theater.objects.filter(name=name).filter(city=city)
        else:
            objects = Theater.objects.filter(name=name)
    else:
        objects = Theater.objects.filter(city=city)

    if objects.count() == 0:
        message = 'No theaters by that name or in that city'
        return render(request, 'regTheaterLocator/search.html', {'message': message})

    if objects.count() > 1:
        context = { 'entries': objects.all() }
        return render(request, 'regTheaterLocator/results.html', context)

    theater = objects.all()[0]
    context = {}
    context = generateTheaterContext(theater)
    return render(request, 'regTheaterLocator/profile.html', context)


def showSearch(request):
    if not 'date' in request.GET and not 'city' in request.GET:
        return render(request, 'regTheaterLocator/list.html', {})
        
    date = request.GET.get('date')
    place = request.GET.get('city')
    #if date:
        
 #       if city:
#            objects = Production.objects.filter(date=date)
 #       else:
#            objects = Production.objects.filter(date=date)
    #else:
    objects = Production.objects.filter(theater__city = place)
    #objects = Production.objects.select_related('theater__city').filter(city=place)

    if objects.count() == 0:
        message = 'No theaters by that name or in that city'
        return render(request, 'regTheaterLocator/results.html', {'message': message})


    context = { 'theaters': objects.all() }
    return render(request, 'regTheaterLocator/results.html', context)


@login_required    
def theaterProfile(request):
    theat = request.GET.get('theater')
    context = generateTheaterContext(Theater.objects.get(theat.name))
    return render(request, 'regTheaterLocator/profile.html', context)

@transaction.atomic
def editProfile(request, id):
    context = {}
    theater = Theater.objects.get(id=id)
    if not theater.admin == request.user:
        return render(request, 'regTheaterLocator/failedPermissions.html', context)
        
    if request.method == 'GET':

        theater = Theater.objects.get(id=id)
        form = EditTheaterForm(instance=theater)
        productions = Production.objects.filter(theater=theater)
        context['form'] = form
        context['theater'] = theater
        context['productions'] = productions
        context['title'] = 'from get'

        return render(request, 'regTheaterLocator/profileEdit.html', context)


    theater = Theater.objects.select_for_update().get(id=id)
    db_update_time = theater.update_time  # Copy timestamp to check after form is bound
    form = EditTheaterForm(request.POST, instance=theater)
    productions = Production.objects.filter(theater=theater)
    if not form.is_valid():
        print(form.errors)
        context = { 'theater': theater, 'form': form, 'title': 'broken', 'message': 'Invalid edits', 'productions': productions }
        return render(request, 'regTheaterLocator/profileEdit.html', context)

    theater.admin = request.user
    form.save()
    productions = Production.objects.filter(theater=theater)
    context = {
            'message': 'Information updated.',
            'theater':   theater,
            'form':    form,
            'productions': productions
        }

    return render(request, 'regTheaterLocator/profileEdit.html', context)


@login_required    
def manageTheaters(request):
    context ={}
    user = request.user
    theaters = Theater.objects.filter(admin=user)
    context['theaters'] = theaters
    return render(request, 'regTheaterLocator/manage.html', context)

    
def createTheater(request):
    context = {}
    if request.method == 'GET':
        context['form'] = CreateTheaterForm()
        return render(request, 'regTheaterLocator/createTheater.html', context)
    
    theater = Theater(admin=request.user, update_time=datetime.now())
    theaterForm = CreateTheaterForm(request.POST, instance=theater)
    if not theaterForm.is_valid():
        context = { 'form': theaterForm, 'title': "salkjfdlkds"}
        return render(request, 'regTheaterLocator/createTheater.html', context)
    theater.admin = request.user
    theaterForm.save()
    productions = Production.objects.filter(theater=theater)
    context = {
            'message': 'Theater Created, Edit here:',
            'theater':   theater,
            'form':    theaterForm,
            'productions': productions
        }

    return render(request, 'regTheaterLocator/profileEdit.html', context)
    context = { 'form': theaterForm, 'title': "Itworked"}

def createProd(request):
    context = {}
    if request.method == 'GET':
        context['form'] = CreateTheaterForm()
        context['theater'] = Theater.objects.get(id = request.GET.get('theater'))
        return render(request, 'regTheaterLocator/createProd.html', context)
    
    theater = Theater.objects.get(id = request.POST.get('theater'))
    production = Production(theater=theater, creation_time=datetime.now())
    
    prodForm = CreateProdForm(request.POST , instance = production)
    if not prodForm.is_valid():
        context = { 'form': prodForm, 'title': "salkjfdlkds", 'message': prodForm['opens']}
        return render(request, 'regTheaterLocator/createTheater.html', context)
    
    production.theater=theater
    production.creation_time=datetime.now()
    prodForm.save()
    return render(request, 'regTheaterLocator/manage.html', {})
    
def manageShow(request):
   return render(request, 'regTheaterLocator/showDates.html', {})
    

@login_required   
def list(request):
   return render(request, 'regTheaterLocator/list.html', {})

def login(request):
    return render(request, 'regTheaterLocator/login.html', {})

def register(request):
    context = {}
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'regTheaterLocator/register.html', context)

    form = RegistrationForm(request.POST)
    context['form'] = form

     # Validates the form.
    if not form.is_valid():
        return render(request, 'regTheaterLocator/register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password1'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
    auth_login(request, new_user)
    return redirect('/list')
