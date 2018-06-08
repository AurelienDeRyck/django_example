import operator
from functools import reduce

from django.db import transaction
from django.db.models import Q
from django.forms import modelformset_factory, formset_factory
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls.base import reverse_lazy, reverse
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin, FormView
from django.views.generic.list import ListView

from ave_cesar.forms import ProductForm, SearchForm, CategoryFormSet
from ave_cesar.models import Product, Category


def home(request):
    return render(request, "home.html")


class ProductListView(FormMixin, ListView):
    model = Product
    form_class = SearchForm
    paginate_by = 5
    def get_queryset(self):
        result = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            result = result.filter(name__icontains=name)

        category = self.request.GET.get('category')
        if category:
            result = result.filter(category=category)

        borrowed = self.request.GET.get('borrowed')
        if borrowed:
            result = result.exclude(borrower=None)

        return result

    def get_initial(self):
        return self.request.GET


class ProductDetailView(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'


class CategoryFormSetView(View):
    category_FormSet=CategoryFormSet
    template_name = 'ave_cesar/category_formset.html'

    def get(self, request, *args, **kwargs):
        context = {
            'category_form': self.category_FormSet,
        }

        return render(request, self.template_name, context)

    # Overiding the post method
    def post(self, request, *args, **kwargs):
        category_formset = self.category_FormSet(self.request.POST)
        # Checking the if the form is valid
        if category_formset.is_valid():
            category_formset.save()
            return HttpResponseRedirect(reverse("category_list"))

class CategoryFormset(FormView):
   form_class = modelformset_factory(Category, fields='__all__')
   template_name = 'ave_cesar/category_formset.html'
   success_url = reverse_lazy('category_list')


class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
