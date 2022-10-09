from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==product.id:
            print(id,product.id)
            return cart.get(id)
        else:
            return 1

@register.filter(name='product_qty')
def product_qty(product, cart):
    prod = (str(product.id))
    qty = cart.get(prod)
    return qty

@register.filter(name='product_total_price')
def product_total_price(product, cart):
    prod_price = (str(product.price))
    prod = (str(product.id))
    qty = cart.get(prod)
    total = int(prod_price) * int(qty)
    return total

@register.filter(name='product_price_cart')
def product_price_cart(products, cart):
    sum = 0
    for product in products:
        sum += product_total_price(product, cart)
    return sum

@register.filter(name='currency_symbol')
def currency_symbol(product):
    return '₹'+str(product)


@register.filter(name='multiply')
def multiply(price, qty):
    return price*qty