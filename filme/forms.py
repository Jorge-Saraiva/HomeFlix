# Criação de formulários personalizados

from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)

# Replicar a criação do formulário que o Django fornece, para Usuário
class CriarContaForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')  # necessário a senha ser nesse padrão, para que o Django reconheça






















