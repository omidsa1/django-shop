from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser

# Customer, product and order models


class Product(models.Model):
    name = models.CharField(max_length=100)
    # to be decided if we want to choose from a tuple (limited list) or
    # go with simple CharField
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    # same dilema as with brand
    category = models.ManyToManyField("Category")

    price = models.ForeignKey("Price", on_delete=models.CASCADE)

    order = models.ManyToManyField("Order", related_name="products")

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Price(models.Model):
    currency_choices = (
        ("USD", "United States Dollars"),
        ("EUR", "Euro"),
        ("IRI", "Iran Rial"),
    )

    price = models.DecimalField(decimal_places=2, max_digits=10)
    currency_of_price = models.CharField(max_length=3, choices=currency_choices)


class Order(models.Model):
    product = models.ManyToManyField("Product", related_name="orders")


class Profile(AbstractUser):
    USER_TYPE_CHOICES = (
        (0, "customer"),
        (1, "admin"),
    )

    user_type = models.BooleanField(choices=USER_TYPE_CHOICES, default=0)
