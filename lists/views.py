from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.views.generic import FormView, CreateView, DetailView

from lists.models import Item, List
from lists.forms import ItemForm, ExistingListItemForm


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


class ViewAndAddToList(DetailView, CreateView):
    model = List
    template_name = 'list.html'
    form_class = ExistingListItemForm

    def get_form(self):
        self.object = self.get_object()
        return self.form_class(for_list=self.object, data=self.request.POST)


class NewListView(CreateView):
    form_class = ItemForm
    template_name = 'home.html'

    def form_valid(self, form):
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
