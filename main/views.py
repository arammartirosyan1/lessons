from django.shortcuts import render, get_object_or_404
from .models import Languages, Types


def index(request):
    posts = Languages.objects.all()
    return render(request, 'index.html', {'posts': posts})


def language(request, language_id):
    name = get_object_or_404(Languages, pk=language_id)
    return render(request, 'language.html', {'name': name})


def detail(request, detail_id):
    posts = Types.objects.get(pk=detail_id)
    return render(request, 'detail.html', {'posts': posts})

