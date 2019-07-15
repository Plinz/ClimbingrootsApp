from django.views import generic
from .models import Crag, Route, NameStory, Anecdote


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


class IndexRouteView(generic.DetailView):
    model = Route
    template_name = 'crags/route_index.html'


class ResultsCragView(generic.DetailView):
    model = Crag
    template_name = 'crags/detail.html'


class IndexAnecdoteView(generic.ListView):
    model = Anecdote
    template_name = 'crags/index.html'
    context_object_name = 'anecdote_list'
    paginate_by = 15


class DetailAnecdoteView(generic.DetailView):
    model = Anecdote


class CreateAnecdoteView(generic.TemplateView):
    model = Anecdote
    template_name = 'crags/anecdote_create.html'


class DetailNameStoryView(generic.DetailView):
    model = NameStory
#   template_name = 'stories/name_story_detail.html'
