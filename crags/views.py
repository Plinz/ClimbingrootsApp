from django.views import generic
from .models import Crag, Route


class IndexCragView(generic.ListView):
    model = Crag
    paginate_by = 15


class DetailCragView(generic.DetailView):
    model = Crag

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        #crag = Crag.objects.get(id=self.kwargs.get('pk', ''))
        # Add in a QuerySet of all the books
        context['route_list'] = self.object.route_set.all()
        return context


class DetailRouteView(generic.DetailView):
    model = Route


class ResultsView(generic.DetailView):
    model = Crag
    template_name = 'crags/detail.html'
