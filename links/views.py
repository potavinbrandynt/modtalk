from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Link, Vote

class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()