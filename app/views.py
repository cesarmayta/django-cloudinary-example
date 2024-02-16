from django.shortcuts import render, redirect
from .forms import ProductoForm

def subir_imagen(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subir_imagen')
    else:
        form = ProductoForm()
    return render(request, 'subir_imagen.html', {'form': form})
