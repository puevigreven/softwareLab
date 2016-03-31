from django import forms
from models import Medicine


class InventoryForm(forms.ModelForm):

	class Meta:
		model = Medicine
		fields = ('medicine_name', 'expiry_data', 'quantity','price')
