from django.contrib import admin
from .models import Item, CartItems, Reviews
from django.db import models


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "created_by", "title", "description", "price", "labels")


class CartItemsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "item",
        "quantity",
        "ordered",
        "ordered_date",
        "delivery_date",
        "status",
    )
    list_filter = ("ordered", "ordered_date", "status")


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("user", "item", "review", "posted_on")


admin.site.register(Item, ItemAdmin)
admin.site.register(CartItems, CartItemsAdmin)
admin.site.register(Reviews, ReviewsAdmin)
