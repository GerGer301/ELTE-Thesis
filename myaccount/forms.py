from django import forms
from .models import User

class profileForm(forms.ModelForm):

    class Meta:
        model = User

        fields = ['nickname', 'first_name', 'last_name', 'telephone', 'lottery_type']
