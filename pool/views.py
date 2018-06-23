from django.shortcuts import render


def index(request):
    return render(request, 'pool/userprofile.html')
