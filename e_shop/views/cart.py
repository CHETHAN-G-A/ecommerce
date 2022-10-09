from django.shortcuts import render, redirect
from e_shop.models import Product
from django.views import View


class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')
        if cart:
            products_id = list(cart.keys())
            products = Product.objects.filter(id__in = products_id)
            return render(request,'cart.html',{'products':products})
        else:
            return render(request, 'cart.html')

    def post(self, request):
        product_id = request.POST.get('product')
        cart = request.session.get('cart')
        del request.session['cart'][product_id]
        request.session.modified = True
        return redirect('cart')



