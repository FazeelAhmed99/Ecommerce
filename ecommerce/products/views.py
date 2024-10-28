from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, SizeVariant, ColorVariant
from accounts.models import Cart, CartItems, Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here.

def get_product(request, slug):
    try:
        print("slug"+slug)
        product = Product.objects.get(slug=slug)
        context = {'product': product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            
        if request.GET.get('color'):
            color = request.GET.get('color')
            price = product.get_product_price_by_color(color)
            context['selected_color'] = color
            context['updated_price'] = price
        
            
        return render(request, 'product/product.html', context=context)
    except Exception as e:
        print(e)
        

def  add_to_cart(request, uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid = uid)
    user = request.user
    cart, _=Cart.objects.get_or_create(user=user, is_paid = False)
    
    cart_item = CartItems.objects.create(cart = cart, product=product)
    
    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name = variant)
        cart_item.size_variant = size_variant
        cart_item.save()
    
        
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

