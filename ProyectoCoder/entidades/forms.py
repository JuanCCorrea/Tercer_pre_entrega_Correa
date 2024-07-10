from django import forms

class clasesForm(forms.Form):
    clases = forms.CharField(max_length=50, required = True)
    valor = forms.IntegerField(required=True)
    
class horarioForm(forms.Form):
    horario = forms.TimeField(required=True)

class ReservaForm(forms.Form):
        nombre = forms.CharField(max_length=50)
        apellido = forms.CharField(max_length=50)
        email = forms.EmailField()
        fecha = forms.DateField()
    