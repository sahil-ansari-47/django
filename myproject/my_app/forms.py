from django import forms

from .models import Reservation

class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Select time'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select date'}),
        }