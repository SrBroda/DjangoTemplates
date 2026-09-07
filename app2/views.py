from django.shortcuts import render


def app2v1(request):
    return render(request, 'app2/v1.html')

def app2v2(request):
    return render(request, 'app2/V2.html')
# Create your views here.
