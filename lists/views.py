from django.shortcuts import render


def lists_page(request):
    return render(request, 'lists/home.html')
