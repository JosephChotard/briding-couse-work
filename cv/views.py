from django.shortcuts import render, get_object_or_404

from .models import Cv

# Create your views here.


def cv_page(request):
    cv = Cv.objects.get(pk=1)

    return render(request, 'cv.html', {'cv': cv})
