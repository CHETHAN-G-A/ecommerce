from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views.login import Login
from .views.signup import Signup
from .views.login import Login , logout
from .views.home import Store
from .views.cart import Cart
from .views.check_out import Check_out
from .views.orders import Orders
from .views.category import Head_phones , Ear_Buds , Ear_phones

urlpatterns = [
    path('', Store.as_view(),name='store'),
    path('head_phones', Head_phones.as_view(), name='Head_phones'),
    path('ear_buds', Ear_Buds.as_view(), name='ear_buds'),
    path('ear_phones', Ear_phones.as_view(),name='ear_phones'),
    path('signin', Signup.as_view(),name='signin'),
    path('login', Login.as_view() , name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(),name='cart'),
    path('check_out', Check_out.as_view(),name='check_out'),
    path('orders', Orders.as_view(),name='orders'),
]

urlpatterns = urlpatterns + static ( settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)