from django.shortcuts import render


def hello_world(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')