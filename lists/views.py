from django.shortcuts import render
from django.http import HttpResponse


def lists_page(request):
    return HttpResponse('<!DOCTYPE html><html><title>Joe\'s To-Do list</title></html>')
