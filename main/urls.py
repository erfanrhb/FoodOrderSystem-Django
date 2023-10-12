from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.MenuListView.as_view(), name="home"),
    path("dishes/<slug>", views.MenueDetail.as_view(), name="dishes"),
    path("item_list/", views.item_list, name="item_list"),
    path("item/new/", views.ItemCreateView.as_view(), name="item-create"),
    path("item-update/<slug>/", views.ItemUpdateView.as_view(), name="item-update"),
    path("item-delete/<slug>/", views.ItemDeleteView.as_view(), name="item-delete"),
    path("add-to-cart/<slug>/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.get_cart_items, name="cart"),
    path(
        "remove-from-cart/<int:pk>/",
        views.CartDeleteView.as_view(),
        name="remove-from-cart",
    ),
    path("ordered/", views.order_item, name="ordered"),
    path("order_details/", views.order_details, name="order_details"),
    path("admin_view/", views.admin_view, name="admin_view"),
    path("pending_orders/", views.pending_orders, name="pending_orders"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("update_status/<int:pk>", views.update_status, name="update_status"),
    path("postReview", views.AddReview.as_view(), name="add_reviews"),
]
