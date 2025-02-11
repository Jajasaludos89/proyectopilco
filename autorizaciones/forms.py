from django import forms
from .models import Proyecto, Autorizacion, Municipio, Condicion

class AutorizacionForm(forms.ModelForm):
    class Meta:
        model = Autorizacion
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'autorizacion', 'aprobado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'autorizacion': forms.Select(attrs={'class': 'form-control'}),
            'aprobado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_autorizacion(self):
        autorizacion = self.cleaned_data.get('autorizacion')
        if Proyecto.objects.filter(autorizacion=autorizacion, aprobado=True).exists():
            raise forms.ValidationError("Esta autorización ya ha aprobado otro proyecto.")
        return autorizacion

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['nombre', 'cid', 'telefono', 'proyectos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cid': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'proyectos': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        }

class CondicionForm(forms.ModelForm):
    class Meta:
        model = Condicion
        fields = ['nombre', 'descripcion', 'municipio', 'proyecto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
        }
