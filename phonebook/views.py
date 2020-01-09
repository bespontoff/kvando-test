from django.shortcuts import render, HttpResponse
from django.views import generic
from django.db.models import Q
from . import models
from . import forms


# Create your views here.


class IndexView(generic.ListView):
    model = models.Entry


class EntryDetailView(generic.DetailView):
    model = models.Entry


class EntryAddView(generic.edit.CreateView):
    form_class = forms.EntryForm
    template_name = 'phonebook/entry_form.html'
    success_url = '/detail/{id}'


class EntryEditView(generic.edit.UpdateView):
    model = models.Entry
    form_class = forms.EntryForm
    template_name = 'phonebook/entry_form.html'
    success_url = '/detail/{id}'


class EntryDeleteView(generic.DeleteView):
    model = models.Entry
    success_url = '/'


class EntrySearchView(generic.ListView):
    model = models.Entry
    template_name = 'phonebook/entry_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        object_list = models.Entry.objects.filter(Q(name__icontains=query) | Q(phone__icontains=query))
        return object_list