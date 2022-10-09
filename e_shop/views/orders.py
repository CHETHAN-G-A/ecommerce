from django.shortcuts import render, redirect
from e_shop.models import Order
from django.views import View
from e_shop.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class Orders(View):

    @method_decorator(auth_middleware)
    def get(self, request):
        customer_id = request.session.get('customer_id')
        orders = Order.objects.filter(customer = customer_id).order_by('-date')
        print(orders)

        return render(request,'orders.html',{'products':orders})