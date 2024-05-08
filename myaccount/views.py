from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from myaccount import models
from apps.models import LotteryTicket

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from myaccount.forms import profileForm

import json
import base64

FORMATTED_TITLE = 'myaccount'

@login_required
def profile(request):
    user = request.user
    tickets = LotteryTicket.objects.filter(user=user)
    total_tickets = tickets.count() # Total number of tickets
    total_spending = sum([ticket.price for ticket in tickets]) # Total spending
    total_winnings = sum([ticket.won_amount for ticket in tickets]) # Total winnings
    total_earnings = total_winnings - total_spending # Total profit
    return render(request, 'myaccount/profile.html', {'user': user, 'formatted_title': FORMATTED_TITLE, 'total_tickets': total_tickets, 'total_spending': f'¥{total_spending}', 'total_winning': f"¥{total_winnings}", 'total_earnings': f'¥{total_earnings}'})

@login_required
@csrf_exempt
def profile_update(request):
    ''' Update user profile '''
    if request.method == 'POST':
        # instance is used to update the current user
        form = profileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # Add a success message
            # messages.add_message(request, messages.SUCCESS, 'Personal info updated successfully!')
            return redirect('myaccount:profile')
    else:
        # Return empty form if the method is not POST
        form = profileForm(instance=request.user)

    return render(request, 'myaccount/change-profile.html', context={'form': form, 'formatted_title': FORMATTED_TITLE})

@login_required
def main_page(request):
    return profile(request)
