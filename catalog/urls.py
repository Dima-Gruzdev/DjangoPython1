
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView

app_name = CatalogConfig.name
urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
