from django.shortcuts import render


def about(request):
    return render(request, 'infopages/about.html')


def faq(request):
    return render(request, 'infopages/faq.html')


def shipping(request):
    return render(request, 'infopages/shipping.html')