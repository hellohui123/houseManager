# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index_view(request):
    print 'hao'
    return render(request,'base.html',{'num':'111111111'})