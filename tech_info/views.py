from django.shortcuts import render

def home(request):
    return render(request, 'tech_info/home.html')

def about(request):
    return render(request, 'tech_info/about.html')

def contact(request):
    return render(request, 'tech_info/contact.html')