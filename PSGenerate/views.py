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
    length = request.GET.get('length')
    is_upper_case = request.GET.get('uppercase')
    is_lower_case = request.GET.get('lowercase')
    for i in range(int(length)):
        password += random.choice(main_word)
    return render(request, 'generated_password.html', {'password': password})




