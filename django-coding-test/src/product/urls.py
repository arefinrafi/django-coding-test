from django.urls import path, include
from product.views.product import CreateProductView, AllProductView, UpdateProductView
from product.views.variant import VariantView, VariantCreateView, VariantEditView
from product.views.api_view import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('create/product', ProductCreateViewSet, basename='product.create')
app_name = "product"

urlpatterns = [
    path('api/', include(router.urls)),
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path("list/", AllProductView.as_view(), name='list.product'),
    path("update/<int:product_id>/", UpdateProductView.as_view(), name='update.product')
    # path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
    #     'product': True
    # }), name='list.product'),
]
