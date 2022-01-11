from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

