from django.views.generic import View, TemplateView, ListView, DetailView
from .models import Flower

class HomeView(ListView):
    template_name = 'home.html'
    model = Flower
    context_object_name = 'flowers'
    paginate_by=3

class FlowerDetailView(DetailView):
    template_name = 'detail.html'
    model = Flower
    context_object_name = 'flower'    