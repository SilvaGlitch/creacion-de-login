# recepcion/forms.py
from django import forms
from .models import Cliente, Equipo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@email.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56 9 1234 5678'}),
        }
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.replace(' ', '').replace('+', '').isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números")
        return telefono

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['cliente', 'tipo_equipo', 'marca', 'modelo', 'problema_reportado']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo_equipo': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: HP, Dell, Lenovo'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Pavilion, ThinkPad'}),
            'problema_reportado': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describa el problema...'}),
        }