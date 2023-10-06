from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'clientes': 'eo'
    }

    # Render the HTML template main.html with the data in the context variable
    return render(request, 'main.html', context=context)

