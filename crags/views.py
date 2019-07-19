from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Crag, Route, NameStory, Anecdote
from crags.enums import RouteType, Grade
from django_countries.fields import CountryField
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

class HomeView(generic.TemplateView):
    template_name = 'crags/home.html'


class IndexCragView(generic.ListView):
    model = Crag
    template_name = 'crags/crag_index.html'


class DetailCragView(generic.DetailView):
    model = Crag
    template_name = 'crags/crag_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        #crag = Crag.objects.get(id=self.kwargs.get('pk', ''))
        # Add in a QuerySet of all the books
        context['route_list'] = self.object.route_set.all()
        return context


class IndexRouteView(generic.DetailView):
    model = Route
    template_name = 'crags/route_detail.html'


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


class DetailNameStoryView(generic.DetailView):
    model = NameStory
#   template_name = 'stories/name_story_detail.html'


class AnecdoteForm(forms.Form):
    anecdote = forms.CharField(label=_("Anecdote"), max_length=5000, widget=forms.Textarea)
    source = forms.CharField(label=_("Source"), max_length=500)


class NameStoryForm(forms.Form):
    story = forms.CharField(label=_("Story"), max_length=5000, widget=forms.Textarea)
    source = forms.CharField(label=_("Source"), max_length=500)


class CragForm(forms.Form):
    name = forms.CharField(label=_("Name"), max_length=500)
    country = CountryField().formfield()


class RouteForm(forms.Form):
    name = forms.CharField(label=_("Name"), max_length=500)
    type = forms.ChoiceField(label=_("Type"), choices=RouteType.choices())
    description = forms.CharField(label=_("Description"), max_length=5000, widget=forms.Textarea)
    openIn = forms.DateField(label=_("Opening date"), widget=forms.SelectDateWidget)
    faIn = forms.DateField(label=_("First ascent date"), widget=forms.SelectDateWidget)


@login_required
def add_anecdote_view(request, pk_crag, pk_route):
    route = get_object_or_404(Route, pk=pk_route)
    if request.method == 'POST':
        form = AnecdoteForm(request.POST)
        if form.is_valid():
            a = Anecdote(route=route, anecdote=form.cleaned_data['anecdote'],
                         source=form.cleaned_data['source'], isValidated=False)
            a.save()
            return HttpResponseRedirect(reverse('crags:route_detail', args=[pk_crag, pk_route]))

    else:
        form = AnecdoteForm()

    return render(request, 'crags/anecdote_create.html', {'form': form, 'route': route})


@login_required
def add_name_story_view(request, pk_crag, pk_route):
    route = get_object_or_404(Route, pk=pk_route)
    if request.method == 'POST':
        form = NameStoryForm(request.POST)
        if form.is_valid():
            n = NameStory(route=route, story=form.cleaned_data['story'],
                          source=form.cleaned_data['source'], isValidated=False)
            n.save()
            return HttpResponseRedirect(reverse('crags:route_detail', args=[pk_crag, pk_route]))

    else:
        form = NameStoryForm()

    return render(request, 'crags/name_story_create.html', {'form': form, 'route': route})


@login_required
def add_crag_view(request):
    if request.method == 'POST':
        form = CragForm(request.POST)
        if form.is_valid():
            n = Crag(name=form.cleaned_data['name'], country=form.cleaned_data['country'], isValidated=False)
            n.save()
            return HttpResponseRedirect(reverse('crags:crags_index'))

    else:
        form = CragForm()

    return render(request, 'crags/crag_create.html', {'form': form})


@login_required
def add_route_view(request, pk_crag):
    crag = get_object_or_404(Crag, pk=pk_crag)
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            n = Route(name=form.cleaned_data['name'], crag=crag, type=form.cleaned_data['type'],
                      openIn=form.cleaned_data['openIn'], description=form.cleaned_data['description'],
                      faIn=form.cleaned_data['faIn'], isValidated=False)
            n.save()
            return HttpResponseRedirect(reverse('crags:route_detail', args=[pk_crag, n.id]))

    else:
        form = RouteForm()

    return render(request, 'crags/route_create.html', {'form': form, 'crag': crag})
