from .views import *
from django.urls import path

app_name = "ecomapp"
urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("about/",AboutView.as_view(),name="about"),
    path("contact-us/",ContactView.as_view(),name="Contact Us:-"),
    path("all-products/",AllProductView.as_view(),name="allproducts"),
    path("product/<slug:slug>/",ProductDetailView.as_view(),name="productdetail"),
    path("add-to-cart-<int:product_id>/",AddToCartView.as_view(),name="addtocart"),
    path("my-cart/",MyCartView.as_view(),name="mycart"),

]
