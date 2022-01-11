from django.shortcuts import render
from django.views.generic import  ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Snack
# Create your views here.
class SnackListView(ListView):
    template_name='snacks/snack-list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name='snacks/snack-detail.html'
    model = Snack
    #fields = ['title','purchaser','description']