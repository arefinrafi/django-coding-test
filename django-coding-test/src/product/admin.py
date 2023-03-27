from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Variant)
admin.site.register(Product)
admin.site.register(ProductImage)


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = [
        "variant_title",
        "variant",
        "product",
    ]


admin.site.register(ProductVariant, ProductVariantAdmin)


class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = [
        "product_variant_one",
        "product_variant_two",
        "product_variant_three",
        "price",
        "stock",
        "product"
    ]


admin.site.register(ProductVariantPrice, ProductVariantPriceAdmin)
