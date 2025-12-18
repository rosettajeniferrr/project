from django.shortcuts import render

def medshots(request):
    return render(request, 'medico.html')
