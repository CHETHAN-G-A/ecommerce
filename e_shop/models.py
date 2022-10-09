from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default=0)
    image = models.ImageField(upload_to='products_img/')


    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(default=0)
    e_mail = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100,null=False)

    def get_customer_by_email(e_mail):
        try:
            return Customer.objects.get(e_mail=e_mail)
        except:
            return False


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models. IntegerField()
    address = models.CharField(max_length=100 , default='', blank=True)
    phone = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)