from django.views import generic
from .models import Anecdote, NameStory


class IndexView(generic.ListView):
    model = Anecdote
    template_name = 'stories/index.html'
    context_object_name = 'anecdote_list'
    paginate_by = 15


class DetailAnecdoteView(generic.DetailView):
    model = Anecdote


class DetailNameStoryView(generic.DetailView):
    model = NameStory
#   template_name = 'stories/name_story_detail.html'
