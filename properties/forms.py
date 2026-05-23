from django import forms
from .models import Property


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