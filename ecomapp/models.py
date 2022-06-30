from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    joined_on = models.DateTimeField
    def __str__(self):
        return self.full_name


class Category (models.Model):
    title = models.CharField(max_length=200,null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title=models.CharField(max_length=200,null=True)
    slug = models.SlugField(unique=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="products",null=True)
    marked_price = models.PositiveIntegerField(null=True)
    selling_price = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True)
    warranty = models.CharField(max_length=300,null=True,blank=True)
    return_policy = models.CharField(max_length=300,null=True,blank=True)
    view_count = models.PositiveIntegerField(default=0,null=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    total= models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart:" +str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart" +str(self.cart.id) + "CartProduct: " + str(self.id)

ORDER_STATUS = (
    ("Order Received","Order Received"),
    ("Order Processing","Order Processing"),
    ("On the way","On the way"),
    ("Order Completed","Order Completed"),
    ("Order Canceled","Order Canceled"),

)


class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=50,null=True)
    shipping_address = models.CharField(max_length=300,null=True)
    mobile = models.CharField(max_length=10,null=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order: " + str(self.id)


