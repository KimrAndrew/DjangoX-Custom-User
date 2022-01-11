from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import  ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Snack
# Create your views here.
class SnackListView(ListView):
    template_name='snacks/snack-list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name='snacks/snack-detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snacks/snack-create.html'
    model = Snack
    fields = ['title','purchaser','description']

class SnackDeleteView(DeleteView):
    template_name='snacks/snack-delete.html'
    model = Snack
    success_url = reverse_lazy('snacks/snack-list')