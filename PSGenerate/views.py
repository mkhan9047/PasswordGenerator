# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def blog(request):
    return render(request, 'blog.html')


def generated_password(request):
    main_word = 'abcdefghijklmnopqrstuvwxyz'
    password = ''
    for i in range(10):
        password += random.choice(main_word)
    return render(request, 'generated_password.html', {'password': password})




