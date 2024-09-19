from django.shortcuts import render, redirect
from .forms import EventForm, RegistrationForm
from .models import Event
from django.db.models import Q
from django.contrib.auth import login, logout

def main_page(request):

    query = request.GET.get('query')

    if query:
        events = Event.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query))

    else:
     events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:main_page')  # Redirect to the main page after saving
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})

def sign_up(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect('mainapp:main_page')
        else:
            return render (request, 'registration/sign_up.html', {'form': form})

    else:
        
        form = RegistrationForm()
        return render(request, 'registration/sign_up.html', {'form': form})

def logout_user(request):
    logout(request)

    return redirect('mainapp:main_page')        



