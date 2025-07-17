
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
app_name = CatalogConfig.name
