from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Zdjęcie',  widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}),)

def validate_username(value):
    if not value.isalnum():
        raise ValidationError('Użyj tylko liter i cyfr.')

class RegistrationForm(UserCreationForm):
    confirm_password = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Nazwa użytkownika',
            'password1': 'Hasło',
            'password2': 'Potwierdź hasło',
        }

        error_messages = {
            'username': {
                'required': 'To pole jest wymagane.',
                'unique': 'Nazwa użytkownika już istnieje. Wybierz inną nazwę.',
                'invalid': 'Nazwa użytkownika może zawierać jedynie litery i cyfry.',
                'max_length': 'Nazwa użytkownika może mieć maksymalnie 150 znaków.',
            },
            'password1': {
                'min_length': 'Hasło musi mieć co najmniej 8 znaków.',
                'password_mismatch': 'Hasła nie pasują do siebie.',
            },
            'password2': {
                'required': 'To pole jest wymagane.',
            },
        }


    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password and confirm_password and password != confirm_password:
    #         raise ValidationError('Hasła nie są identyczne.')