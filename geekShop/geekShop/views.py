from django.shortcuts import render

def index(request):
    context = {
        'slogan':'Супер предложение'
    }
    return render(request,'geekShop/index.html', context)

def contacts (request):
    return render(request,'geekShop/contact.html')

