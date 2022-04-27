from django.urls import path, re_path
from .views import *


urlpatterns = [
    path("", overview),
    path("product/create/", add_product),
    path("product/view/", view_products),
    path("product/category/<str:category>/", view_products_by_category),
    path("product/update/<int:pk>/", update_product),
]
