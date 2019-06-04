from django.shortcuts import render
from .forms import ProductForm

from .models import Product
# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    # testando
    #obj = Product.objects.get(id=1)
    obj = Product.objects.latest('id')
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'summary': obj.summary,
    #     'featured': obj.featured,
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

