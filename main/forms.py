from django import forms
from .models import Game
class GameForm(forms.ModelForm):
    
    class Meta:
        model=Game
        fields = [
            'name',
            'price',
            'description',
            'release_date',
            "img1",
            "img2",
            "img3",
            "logo",
            "trailer",
            "genre",
            "creator",
            "rating"
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter game name', 'class':'form-control', 'label': 'Game Name'}),
            'price': forms.NumberInput(attrs= {'placeholder': 'Enter game price', 'class':'form-control', 'label': 'Game Price'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter game description', 'class':'form-control', 'rows': 4}),
            'genre': forms.TextInput(attrs={'placeholder': 'Enter game genre', 'class':'form-control'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'Enter game rating', 'class':'form-control', 'step': '0.1', 'min': '0', 'max': '10'}),
            'release_date': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'creator': forms.TextInput(attrs={'placeholder': 'Enter game creator', 'class':'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'img1': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'img2': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'img3': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'trailer': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
        }
        labels = {
            'img1': 'Картинка 1',
            'img2': 'Картинка 2',
            'img3': 'Картинка 3',
            'logo': 'Логотип',
        }
        

