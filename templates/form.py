from django import forms
from projectApp.models import Flower

class UserForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = "__all__"