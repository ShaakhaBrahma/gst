from django.forms import ModelForm, forms
from .models import Client, R1a


class ClientEntry(ModelForm):

	class Meta:
		model=Client
		fields='__all__'
		allgstin = forms.ModelChoiceField(queryset=Client.objects.raw('SELECT * from Client'))



		

