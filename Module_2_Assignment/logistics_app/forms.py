# logistics_app/forms.py

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        read_only = kwargs.pop('read_only', False)
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        if read_only:
            self.fields['order_id'].widget.attrs['readonly'] = True

    class Meta:
        model = Order
        fields = ['order_id', 'order_date', 'delivery_location', 'client_type']
        widgets = {
            'order_id': forms.TextInput(attrs={'class': 'form-control'}),
            'order_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'delivery_location': forms.TextInput(attrs={'class': 'form-control'}),
            'client_type': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'order_id': 'Order ID',
            'order_date': 'Order Date',
            'delivery_location': 'Delivery Location',
            'client_type': 'Client Type',
        }
