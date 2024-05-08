import random
import json
import numpy as np
import pandas as pd
from django.shortcuts import render
from apps.models import LotteryTicket, HistoricalLotteryTicket
from django.contrib.auth.decorators import login_required

class Prediction:
    def __init__(self, output):
        self.red_1 = output['1']
        self.red_2 = output['2']
        self.red_3 = output['3']
        self.red_4 = output['4']
        self.red_5 = output['5']
        self.red_6 = output['6']
        self.blue_1 = output['7']

FORMATTED_TITLE = 'dashboards'
    
@login_required    
def dashboard(request):

    user = request.user
    tickets = LotteryTicket.objects.filter(user=user)
    total_tickets = tickets.count() # Total number of tickets
    total_spending = sum([ticket.price for ticket in tickets]) # Total spending
    total_winning = sum([ticket.won_amount for ticket in tickets]) # Total winnings
    total_earning = total_winning - total_spending # Total profit

    historical_tickets = HistoricalLotteryTicket.objects.all()
    # Get the historical tickets from last year to this year
    this_year = pd.Timestamp.now().year
    last_year = this_year - 1
    historical_tickets = historical_tickets.filter(draw_date__year__gte=last_year)
    
    # Find the 9 most frequently occuring red numbers
    red_numbers = historical_tickets.values_list('red_1', 'red_2', 'red_3', 'red_4', 'red_5', 'red_6')
    red_numbers = np.array(red_numbers).flatten()
    red_numbers = pd.Series(red_numbers)
    red_numbers = red_numbers.value_counts().head(9)
    red_number_occurences = {red_number: count for red_number, count in red_numbers.items()}

    # Find the 5 most frequently occuring blue numbers
    blue_numbers = historical_tickets.values_list('blue_1')
    blue_numbers = np.array(blue_numbers).flatten()
    blue_numbers = pd.Series(blue_numbers)
    blue_numbers = blue_numbers.value_counts().head(5)
    blue_number_occurences = {blue_number: count for blue_number, count in blue_numbers.items()}

    # Show 3 randomly generated tickets
    random_tickets1 = random.sample(range(1, 34), 6)
    random_tickets2 = random.sample(range(1, 34), 6)
    random_tickets3 = random.sample(range(1, 34), 6)

    output1 = {f'{i + 1}': random_tickets1[i] for i in range(6)}
    output1['7'] = random.randint(1, 16)

    output2 = {f'{i + 1}': random_tickets2[i] for i in range(6)}
    output2['7'] = random.randint(1, 16)

    output3 = {f'{i + 1}': random_tickets3[i] for i in range(6)}
    output3['7'] = random.randint(1, 16)

    context = {'formatted_title': FORMATTED_TITLE,
               'total_tickets': total_tickets,
                'total_spending': total_spending,
                'total_winning': total_winning,
                'total_earning': total_earning,
                'red_number_occurences': json.dumps(red_number_occurences),
                'blue_number_occurences': json.dumps(blue_number_occurences),
                'output1': Prediction(output1),
                'output2': Prediction(output2),
                'output3': Prediction(output3),
               }
    return render(request, 'dashboards/index.html', context)

@login_required
def main_page(request):
    return dashboard(request)