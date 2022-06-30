from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all().order_by("-id")
        context['categories'] = Category.objects.all()
        return context


class AllProductView(TemplateView):
    template_name = 'allproducts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(TemplateView):
    template_name = "productdetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug=self.kwargs['slug']
        product = Product.objects.get(slug=url_slug)
        product.view_count += 1
        product.save()
        context['product'] = product
        return context


class AddToCartView(TemplateView):
    template_name = "addtocart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #get product from requested url
        product_id = self.kwargs['product_id']
        #get product
        product_obj =Product.objects.get(id=product_id)
        #check if cart exists
        cart_id = self.request.session.get("cart_id",None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(
                product=product_obj)
            
            #item already exists in cart
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.selling_price
                cartproduct.save()
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
            #new item is added in cart
            else:
                cartproduct = CartProduct.objects.create(
                    cart=cart_obj,product=product_obj,rate=product_obj.selling_price,quantity=1,subtotal=product_obj.selling_price)
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
                
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id']=cart_obj.id
            cartproduct = CartProduct.objects.create(
                    cart=cart_obj,product=product_obj,rate=product_obj.selling_price,quantity=1,subtotal=product_obj.selling_price)
            cart_obj.total += product_obj.selling_price
            cart_obj.save()
                

        return context
    


class MyCartView(TemplateView):
    template_name = "mycart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id",None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart =None
        context['cart'] = cart           
        return context
    


class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contactus.html'

