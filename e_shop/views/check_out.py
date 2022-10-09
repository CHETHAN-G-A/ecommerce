from django.shortcuts import render, redirect
from e_shop.models import Product , Order , Customer
from django.views import View
from e_shop.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class Check_out(View):
    @method_decorator(auth_middleware)
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.objects.filter(id__in = list(cart.keys()))
        for product in products:
            order = Order(customer=Customer(id = customer),
                          product = product,
                          price = product.price,
                          quantity = cart.get(str(product.id)),
                          address = address,
                          phone = phone)
            order.save()
        request.session['cart']={}
        print(address,phone,customer , products)
        return redirect('cart')
