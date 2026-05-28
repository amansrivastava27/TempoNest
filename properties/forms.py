from django import forms
from .models import Property, Booking


# =========================================
# PROPERTY FORM
# =========================================

class PropertyForm(forms.ModelForm):

    class Meta:

        model = Property

        fields = [
            'title',
            'category',
            'price',
            'location',
            'city',
            'description',
            'image',
            'wifi',
            'parking',
            'food',
            'ac'
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter property title'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Monthly rent price'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Full property location'
                }
            ),

            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'City'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write detailed property description',
                    'rows': 6
                }
            ),

            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }


# =========================================
# BOOKING FORM
# =========================================

class BookingForm(forms.ModelForm):

    class Meta:

        model = Booking

        fields = [
            'phone',
            'message'
        ]

        widgets = {

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone Number'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your booking request',
                    'rows': 5
                }
            )

        }