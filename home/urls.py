from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addToCart', views.addToCart, name='addToCart'),
    path('editaccount', views.editaccount, name='editaccount'),
    path('edit', views.edit, name='edit'),
    path('home', views.home, name='home'),
    path('signuphome', views.signuphome, name='signuphome'),
    path('loginhome', views.loginhome, name='loginhome'),
    path('logouthome', views.logouthome, name='logouthome'),
    path('searching', views.searching, name='searching'),
    re_path(r'^search/(?P<path>.*)$', views.search),
    re_path(r'^description/(?P<path>.*)$', views.description),
    re_path(r'^catagory/(?P<path>.*)$', views.catagories),
    re_path(r'^deleteFromCart/(?P<path>.*)$', views.deleteFromCart),
    re_path(r'^PaymentDone/(?P<path>.*)$', views.PaymentDone),
    re_path(r'^YourOrder/(?P<path>.*)$', views.YourOrder),
    path('account', views.account, name='account'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('cart', views.cart, name='cart'),
]