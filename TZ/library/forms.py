from django import forms
from .models import User, Book

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
