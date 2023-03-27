from django.views import generic
from product.models import Variant, Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class AllProductView(generic.TemplateView):
    model = Product
    template_name = 'products/list.html'


    def get_context_data(self, **kwargs):
        context = super(AllProductView, self).get_context_data(**kwargs)
        product = Product.objects.all().order_by('-id')
        prodvariant = Variant.objects.all()

        search = self.request.GET.get('title', None)
        variant = self.request.GET.get('variant', None)
        filterPrice = self.request.GET.get('price_from', None)
        date = self.request.GET.get('date', None)

        if search:
            product = product.filter(title__icontains = search)
        
        if variant:
            product = product.filter(productvariant__variant_title__icontains = variant)
        
        if filterPrice:    
            filter_price1 = self.request.GET.get('price_from', None)
            filter_price2 = self.request.GET.get('price_to', None)
            if filter_price1 == '' or filter_price2 == '':
                filter_price1=0
                filter_price2=0
            else:
                product = Product.objects.filter(productvariantprice__price__range=(filter_price1,filter_price2))

        if date:
            product = product.filter(created_at__icontains = date)
        
        

        page = self.request.GET.get('page', 1)
        paginator = Paginator(product, 3)
        paged_products = paginator.get_page(page)

        try:
            paged_products= paginator.page(page)
        except PageNotAnInteger:
            paged_products= paginator.page(1)
        except EmptyPage:
            paged_products= paginator.page(paginator.num_pages)

        context['product'] = paged_products
        context['prodvariant'] = prodvariant
        context['product_count'] = product.count()
        
        return context
    
class UpdateProductView(generic.TemplateView):
    template_name = 'products/update.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        context['product_id'] = kwargs.get('product_id')
        return context
