from django.shortcuts import render, redirect
from e_shop.models import Product, Category
from django.views import View

class Store(View):
    def get(self, request):
        category = Category.objects.all()
        products = Product.objects.all()
        return render(request, 'store.html', {'categories': category, 'products': products})

    def post(self, request):

        product_id = request.POST.get('product')
        qty = int(request.POST.get('qty'))
        print(product_id)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                cart[product_id] =  quantity + qty
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = qty
        request.session['cart'] = cart
        print(cart)
        return redirect('store')
