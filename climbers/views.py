from django.views import generic
from .models import Climber


class IndexView(generic.ListView):
    model = Climber
    template_name = 'climbers/index.html'
    context_object_name = 'climber_list'
    paginate_by = 15


class DetailView(generic.DetailView):
    model = Climber
    template_name = 'climbers/detail.html'


class ResultsView(generic.DetailView):
    model = Climber
    template_name = 'climbers/detail.html'


class HomeView(generic.TemplateView):
    template_name = 'climbers/base.html'

