from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    for product in products:
        print("products", product.category)
    
    context = {'products': products}
    return render(request, 'home/index.html', context)

