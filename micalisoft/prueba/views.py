from django.shortcuts import render
from prueba.models import Usuarios
from forms import UsuarioForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def crear(request):
    if request.POST:
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UsuarioForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    usuarios = Usuarios.objects.all()#[:10]
    args['usuarios'] = usuarios
    return render_to_response('crear_usuario.html', args)