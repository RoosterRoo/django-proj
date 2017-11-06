# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import ChoreList
from django.template import loader

# Create your views here.
def index(request):
    lists = ChoreList.objects.all()
    return render(request,'chores/index.html',{'chorelists': lists})

def detail(request,chorelist_id):
    list = get_object_or_404(ChoreList,pk=chorelist_id)
    return render(request,'chores/detail.html',{'chorelist': list})

def chores(request,chorelist_id):
    list = get_object_or_404(ChoreList,pk=chorelist_id)
    return render(request,'chores/chores.html',{'chorelist': list})

def choredetail(request,chorelist_id,chore_id):
    list = get_object_or_404(ChoreList,pk=chorelist_id)
    chore = get_object_or_404(Chore,pk=chore_id)
    return render(request,'chores/choredetail.html',{'chorelist':list,'chore':chore})
