from TechVrDev.models import TechVrDevapp
from django.shortcuts import render
from TechVrDev.models import TechVrDevapp


def TechVrDev(request):
    return render(request, 'techVrDev.html', {})

def TechVrDev_intex(request):
    TechVrDev = TechVrDevapp.objects.all()
    context = {
        'TechVrDev': TechVrDev
    }
    return render(request,'TechVrDev_intex',context)

def TechVrDev_detail(request, pk):
    TechVrDev = TechVrDevapp.objects.get(pk= pk)
    context = {
        'TechVrDevapp' : TechVrDevapp
    }
    return render(request,'TechVrDev_detail.html',context)
