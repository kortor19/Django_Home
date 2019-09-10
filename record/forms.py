from django import forms
from .models import *
from .models import Staff
from .models import Customer



class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields =['first_name', 'last_name', 'dob', 'phoneno', 'email', 'address']


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phoneno', 'address']
