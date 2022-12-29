from django.shortcuts import render

def index(request):
    # name = input("enster u name ")
    # print(name)
    return render(request, 'base/index.html')
