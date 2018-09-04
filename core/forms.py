from django import forms


class ClienteForm(forms.Form):
    seu_nome = forms.CharField(label='Seu nome', max_length=100)

