from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.template import TemplateDoesNotExist

from .models import LotteryTicket, HistoricalLotteryTicket
from .forms import LotteryTicketForm

FORMATTED_TITLE = 'apps'
WINNING_AMOUNT = {
    "first": "¥5,000,000",
    "second": "¥200,000",
    "third": "¥3,000",
    "fourth": "¥200",
    "fifth": "¥10",
    "sixth": "¥5",
    "seventh": "¥0",
}

@login_required
def dynamic_template_apps_view(request, template_name):
    try:
        return render(request, f'apps/{template_name}.html', {'formatted_title': FORMATTED_TITLE})
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html', {'formatted_title': FORMATTED_TITLE})

@login_required    
def dynamic_template_apps_calendar_view(request, template_name):
    try:
        return render(request, f'apps/calendar/{template_name}.html', {'formatted_title': FORMATTED_TITLE})
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html', {'formatted_title': FORMATTED_TITLE})            

@login_required
def ticket_add(request):
    if request.method == 'POST':
        form = LotteryTicketForm(request.POST)
        if form.is_valid():
            # Sort the first 6 numbers
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('apps:ticket_list')
    else:
        form = LotteryTicketForm()
        return render(request, 'apps/lotterytracker/ticket_form.html', {'form': form, 'formatted_title': FORMATTED_TITLE})
    
@login_required
def ticket_edit(request, ticket_id):
    ticket = get_object_or_404(LotteryTicket, user=request.user, id=ticket_id) # Only the user who created the ticket can edit it
    if request.method == 'POST':
        form = LotteryTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('apps:ticket_list')
    else:
        form = LotteryTicketForm(instance=ticket)
        return render(request, 'apps/lotterytracker/ticket_edit.html', {'form': form, 'ticket': ticket, 'formatted_title': FORMATTED_TITLE})

@login_required
def ticket_list(request, order_by='purchase_date'):
    if order_by == 'purchase_date':
        ticket_list = LotteryTicket.objects.filter(user=request.user).order_by('purchase_date')
    else:
        # Order the elements reversely
        ticket_list = LotteryTicket.objects.filter(user=request.user).order_by(f'-{order_by}')
    paginator = Paginator(ticket_list, 10) # Show 10 tickets per page
    page = request.GET.get('page')
    tickets = paginator.get_page(page)
    # for t in tickets:
    #     print(t.blue_1)
    return render(request, 'apps/lotterytracker/ticket_list.html', {'tickets': tickets, 'formatted_title': FORMATTED_TITLE})

@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(LotteryTicket, user=request.user, id=ticket_id)
    ticket.delete()
    return HttpResponse(status=204)

@login_required
def main_page(request):
    return ticket_list(request)

@login_required
def display_historical_lottery(request, order_by='draw_date'):
    query = request.GET.get('draw_id', '')
    if query:
        historical_lottery = HistoricalLotteryTicket.objects.filter(draw_id=query)
    else:
        historical_lottery_list = HistoricalLotteryTicket.objects.all().order_by(f'-{order_by}')
        paginator = Paginator(historical_lottery_list, 20) # Show 20 tickets per page
        page = request.GET.get('page')
        historical_lottery = paginator.get_page(page)
    return render(request, 'apps/lotterytracker/his_list.html', {'tickets': historical_lottery, 'formatted_title': FORMATTED_TITLE})

"""
Winning conditions for the lottery:
    first: 6+1,
    second: 6+0,
    third: 5+1,
    fourth: 4+1 or 5+0,
    fifth: 3+1 or 4+0,
    sixth: 2+1 or 1+1 or 0+1
"""

@login_required
def check_lottery(request):
    winning = ""
    my_ticket = []
    draw_ticket = []
    for i in range(1, 7):
        my_ticket.append(request.GET.get(f'red_{i}', 0))
        draw_ticket.append(request.GET.get(f'draw_red_{i}', 0))
    my_ticket.append(request.GET.get('blue_1', 0))
    draw_ticket.append(request.GET.get('draw_blue_1', 0))
    
    if 0 not in my_ticket and 0 not in draw_ticket:
        # Check the winning conditions
        red_count = 0
        blue_count = 0
        for i in range(6):
            if my_ticket[i] in draw_ticket[:6]:
                red_count += 1
        if my_ticket[6] == draw_ticket[6]:
            blue_count += 1

        if red_count == 6 and blue_count == 1:
            winning = WINNING_AMOUNT["first"]
        elif red_count == 6 and blue_count == 0:
            winning = WINNING_AMOUNT["second"]
        elif red_count == 5 and blue_count == 1:
            winning = WINNING_AMOUNT["third"]
        elif red_count == 4 and blue_count == 1:
            winning = WINNING_AMOUNT["fourth"]
        elif red_count == 5 and blue_count == 0:
            winning = WINNING_AMOUNT["fourth"]
        elif red_count == 3 and blue_count == 1:
            winning = WINNING_AMOUNT["fifth"]
        elif red_count == 4 and blue_count == 0:
            winning = WINNING_AMOUNT["fifth"]
        elif red_count == 2 and blue_count == 1:
            winning = WINNING_AMOUNT["sixth"]
        elif red_count == 1 and blue_count == 1:
            winning = WINNING_AMOUNT["sixth"]
        elif red_count == 0 and blue_count == 1:
            winning = WINNING_AMOUNT["sixth"]
        else:
            winning = WINNING_AMOUNT["seventh"]

    return render(request, 'apps/lotterytracker/lottery_checker.html', {'winning': f"Your ticket has won: {winning}", 'formatted_title': FORMATTED_TITLE})
