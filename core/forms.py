from django import forms

from .models import Producto, Categoria, Etiqueta, DetalleProducto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria', 'etiquetas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Balón Nike Flight'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'etiquetas': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }

class DetalleForm(forms.ModelForm):
    class Meta:
        
        from .models import DetalleProducto 
        # ojo nombre
        model = DetalleProducto
        fields = ['dimensiones', 'peso']
        widgets = {
            'dimensiones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Talla 42'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Kg'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'})}

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'})}