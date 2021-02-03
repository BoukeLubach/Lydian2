from django.shortcuts import render



def kmDistillationView(request):
    
    context = {}
    
    return render(request, 'kmApps/kmDistillation.html', context)
