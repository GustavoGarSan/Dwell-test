from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Ticket
from .forms import TicketForm
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'restaurants/index.html', context)

@login_required(login_url="login")
def restaurants(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'restaurants/restaurants.html', context)
    
@login_required(login_url="login")
def restaurant(request, pk):
    try:
        restaurantObj = Restaurant.objects.get(id=pk)
        countTickets = restaurantObj.ticket_set.count()
        numPurchased = restaurantObj.ticket_set.filter(available=False).count()
        context = {'restaurant': restaurantObj, 'countTickets': countTickets, 'numPurchased': numPurchased}
        return render(request, 'restaurants/single-restaurant.html', context)
    except (Restaurant.DoesNotExist, ValidationError):
        return HttpResponseNotFound('<h1>Page not found</h1>')

@login_required(login_url="login")
def createTicket(request):
    form = TicketForm()
    
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            restaurant = ticket.restaurant
            ticket.save()
            messages.success(request, 'The ticket was created!')
            return redirect('restaurant', pk=restaurant.id)
        
    context = {'form': form}
    return render(request, 'tickets/ticket_form.html', context)

@login_required(login_url="login")
def updateTicket(request, pk):
    try:
        ticket = Ticket.objects.get(id=pk)
        restaurant = ticket.restaurant
        form = TicketForm(instance=ticket)
        
        if request.method == 'POST':
            form = TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('restaurant', pk=restaurant.id)
            
        context = {'form': form}
        return render(request, 'tickets/ticket_form.html', context)
    except (Ticket.DoesNotExist, ValidationError):
        return HttpResponseNotFound('<h1>Page not found</h1>')

@login_required(login_url="login")
def deleteTicket(request, pk):
    try:
        ticket = Ticket.objects.get(id=pk)
        restaurant = ticket.restaurant
        if request.method == 'POST':
            ticket.delete()
            return redirect('restaurant', pk=restaurant.id)
        
        context = {'object': ticket, 'restaurant': restaurant}
        return render(request, 'delete-template.html', context)
    except (Ticket.DoesNotExist, ValidationError):
        return HttpResponseNotFound('<h1>Page not found</h1>')

def purchaseTicket(request, pk):
    try:
        ticket = Ticket.objects.select_for_update().get(id=pk)
        restaurant = ticket.restaurant
        ticketList = restaurant.ticket_set.filter(available=True)
        if request.method == 'POST':
            if ticket.available:
                ticket.available = False
                ticket.save()
                messages.success(request, f'You bought the the ticket "{ticket.name}"')
                return redirect('home')
            else:
                messages.error(request, f'Sorry, the ticket "{ticket.name}" was already purchased')
                return redirect('home')
        
        context = {'restaurant': restaurant, 'ticket': ticket, 'ticketList' : ticketList}
        return render(request, 'tickets/purchase.html', context)
    except (Ticket.DoesNotExist, ValidationError):
        return HttpResponseNotFound('<h1>Page not found</h1>')