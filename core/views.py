from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Product
from core.services import get_products_from_database


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seller_product_count = User.objects.annotate(product_count=Count("selling_products"))
        # result = []
        # for seller in seller_product_count:
        #     result.append({"username": seller.username, "product_count": seller.product_count})
        get_products_from_database()
        result_list = [
            {"username": seller.username, "product_count": seller.product_count}
            for seller in seller_product_count
        ]
        print(result_list)
        context["products"] = Product.objects.all()
        return context

