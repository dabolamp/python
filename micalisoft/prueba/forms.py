from django import forms
from models import Usuarios

class UsuarioForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].label = "Nombre de Usuario"


   class Meta:
      model = Usuarios
      fields = '__all__'
