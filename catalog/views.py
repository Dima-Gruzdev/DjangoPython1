from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page

from catalog.forms import ProductForm
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.services import get_product_from_cache, get_products_by_category


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'

    def get_queryset(self):
        return get_product_from_cache()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Продукт успешно создан.')
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user:
            return HttpResponseForbidden("Вы не можете редактировать этот продукт.")
        return super().dispatch(request, *args, **kwargs)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("Удалить продукт могут только владелец или модератор.")
        return super().dispatch(request, *args, **kwargs)


class ContactsView(TemplateView):
    template_name = 'products/contacts.html'


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав на отмену публикации.")
        product.is_published = False
        product.save()
        messages.success(request, f'Продукт "{product.name}" снят с публикации.')
        return redirect('catalog:product_list')


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductsByCategoryView(TemplateView):
    template_name = 'products/products_by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = kwargs['category_name']  # передаётся из URL

        if not Category.objects.filter(name_cat__iexact=category_name).exists():
            raise Http404("Категория не найдена")
        products = get_products_by_category(category_name)
        context['products'] = products
        context['category_name'] = category_name.title()
        return context