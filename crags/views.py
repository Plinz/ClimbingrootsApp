from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
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


class CreateAnecdoteView(generic.DetailView):
    model = Route
    template_name = 'crags/anecdote_create.html'


class DetailNameStoryView(generic.DetailView):
    model = NameStory
#   template_name = 'stories/name_story_detail.html'


class AnecdoteForm(forms.Form):
    anecdote = forms.CharField(label='Anecdote', max_length=5000, widget=forms.Textarea)
    source = forms.CharField(label='Source', max_length=500)


def add_anecdote_view(request, pk_crag, pk_route):
    route = get_object_or_404(Route, pk=pk_route)
    if request.method == 'POST':
        form = AnecdoteForm(request.POST)
        if form.is_valid():
            a = Anecdote(route=route, anecdote=form.cleaned_data['anecdote'], source=form.cleaned_data['source'], isValidated=False)
            a.save()
            return HttpResponseRedirect(reverse('crags:route_index', args=[pk_crag, pk_route]))

    else:
        form = AnecdoteForm()

    return render(request, 'crags/anecdote_create.html', {'form': form, 'route': route})

