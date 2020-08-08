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
    main_word = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    length = request.GET.get('length', 6)
    is_upper_case = request.GET.get('uppercase')
    is_numbers = request.GET.get('number')
    is_special_char = request.GET.get('special')

    if is_special_char:
        main_word.extend(list('#$%&()*+,-./:;<=>?@[\]^_`{|}~'))
    if is_upper_case:
        main_word.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if is_numbers:
        main_word.extend(list('1234567890'))

    for i in range(int(length)):
        password += random.choice(main_word)
    return render(request, 'generated_password.html', {'password': password})


def author(request):
    return render(request, 'about.html')
