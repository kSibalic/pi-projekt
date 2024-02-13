from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('kategorija', 'naziv', 'opis', 'cijena', 'slika',)
        widgets = {
            'kategorija': forms.Select(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'naziv': forms.TextInput(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'opis': forms.Textarea(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'cijena': forms.TextInput(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border',
                'placeholder': 'U EUR'
            }),
            'slika': forms.FileInput(attrs={
                'class': 'w-full py-4 px-4 rounded-xl border'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('naziv', 'opis', 'cijena', 'slika', 'dostupno')
        widgets = {
            'naziv': forms.TextInput(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'opis': forms.Textarea(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'cijena': forms.TextInput(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'slika': forms.FileInput(attrs={
                'class': 'w-full py-4 px-4 rounded-xl border'
            })
        }