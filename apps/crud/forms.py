from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome','cpf','email','telefone','data_nascimento','sintomas']
        widgets = {
            'nome':forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':"nome",
                    'required':True,
                },
            ),
            'cpf':forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':"cpf",
                    'required':True,
                },
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':"form-control",
                    'id':"email",
                    'required':True,
                },
            ),
        }