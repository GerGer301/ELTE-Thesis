from django import forms
from .models import LotteryTicket

class LotteryTicketForm(forms.ModelForm):
        
        # Sort the first 6 numbers in ascending order
        def clean(self):
            cleaned_data = super().clean()
            red_numbers = [cleaned_data.get('red_1'), cleaned_data.get('red_2'), cleaned_data.get('red_3'), cleaned_data.get('red_4'), cleaned_data.get('red_5'), cleaned_data.get('red_6')]
            red_numbers.sort()
            cleaned_data['red_1'] = red_numbers[0]
            cleaned_data['red_2'] = red_numbers[1]
            cleaned_data['red_3'] = red_numbers[2]
            cleaned_data['red_4'] = red_numbers[3]
            cleaned_data['red_5'] = red_numbers[4]
            cleaned_data['red_6'] = red_numbers[5]
            return cleaned_data
    
        class Meta:
            model = LotteryTicket
    
            fields = ['red_1', 'red_2', 'red_3', 'red_4', 'red_5', 'red_6', 'blue_1', 'purchase_date', 'price', 'won_amount']
