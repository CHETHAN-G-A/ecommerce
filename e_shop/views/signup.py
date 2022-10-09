from django.shortcuts import render, redirect
from e_shop.models import Product, Category ,Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request , "signin.html")

    def post(self, request):
        error_message = None
        if request.method == 'POST':
            ## check if the email already exists ##
            e_mail = request.POST.get('e_mail')
            error_message = None
            if Customer.objects.filter(e_mail=e_mail):
                error_message = "e-mail already exists"
                return redirect("signin")

            else:
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                phone = request.POST.get('phone')
                password = request.POST.get('password')

                # validation#

                if (not first_name):
                    error_message = "First name is required"
                elif (not last_name):
                    error_message = "Last name is required"
                elif (not phone):
                    error_message = "phone number is rerquired"

                else:
                    # hashing password #
                    hashed_password = make_password(password)
                    # ---------------- #
                    customer = Customer(first_name=first_name, last_name=last_name, phone=phone, e_mail=e_mail,
                                        password=hashed_password)
                    customer.save()
                    error_message = "successfully registered"

        return render(request, "signin.html", {'error_message': error_message})
