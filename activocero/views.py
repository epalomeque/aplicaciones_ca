from django.shortcuts import render

# Create your views here.
def cambiaractivo(request):
    context = locals()
    template = 'activocero.html'
    return render(request, template, context)