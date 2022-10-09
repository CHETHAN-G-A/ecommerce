from django.shortcuts import render, redirect
from e_shop.models import Product, Category ,Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Login(View):
    def get(self, request):
        return render(request , "login.html")

    def post(self, request):
        error_message = None
        e_mail = request.POST.get('e_mail')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(e_mail)

        if not customer:
            error_message = "User not registered"
        elif customer and check_password(password, customer.password):
            # adding to session #
            request.session['customer_id'] = customer.id
            request.session['e_mail'] = customer.e_mail
            # ------------------#
            return redirect("store")
        else:
            error_message = "Invalid password"

        return render(request, "login.html", {'error_message': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')