from .models import Funcionario
from django import forms


class InsereFuncionarioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        model = Funcionario

        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao'
        ]
