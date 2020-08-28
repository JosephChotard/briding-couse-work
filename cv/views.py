from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Cv
from .forms import CvForm

# Create your views here.


def cv_page(request):
    first = Cv.objects.first()
    if not first:
        raise Http404
    cv = get_object_or_404(Cv, pk=first.id)

    return render(request, 'cv.html', {'cv': cv})


def cv_edit_page(request):
    if request.user.is_anonymous:
        return redirect('cv_page')
    cv = Cv.objects.first()
    if request.method == 'POST':
        form = CvForm(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save()
            return redirect('cv_page')
    if not cv:
        raise Http404
    form = CvForm(instance=cv)
    return render(request, 'cv-edit.html', {'form': form})
