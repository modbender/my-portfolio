from django.shortcuts import render

from .models import Skill, Profile, Category, Post, Work, Service

def home(request):
    return render(
        request,
        'index.html',
        {
            'profile': Profile.objects.all().order_by('added_at').first(),
            'works': Work.objects.all().order_by('name'),
            'posts': Post.objects.all().order_by('title'),
            'services': Service.objects.all().order_by('name'),
            'categoies': ''
        }
    )
