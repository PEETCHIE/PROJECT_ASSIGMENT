from .models import *
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {'productId', 'productName', 'productBrand', 'productColor', 'productPrice', 'productAmount'}
        widgets = {
                'productId': forms.TextInput(attrs={'class': 'form-control'}),
                'productName': forms.TextInput(attrs={'class': 'form-control'}),
                'productBrand': forms.Select(attrs={'class': 'form-control'}),
                'productColor': forms.RadioSelect(attrs={'class': 'form-control'}),
                'productPrice': forms.NumberInput(attrs={'class': 'form-control', 'min': 100, 'max': 99999}),
                'productAmount': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
        labels = {
            'productId' : 'รหัสสินค้า',
            'productName': 'ชื่อสินค้า',
            'productBrand': 'ยี่ห้อสินค้า',
            'productColor': 'สี',
            'productPrice': 'ราคา',
            'productAmount': 'จำนวน',
        }