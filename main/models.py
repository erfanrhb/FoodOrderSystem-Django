from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Item(BaseModel):
    LABELS = (
        ("پرفروش", "پرفروش"),
        ("جدید", "جدید"),
        ("خوشمزه🔥", "خوشمزه🔥"),
    )

    LABEL_COLOUR = (
        ("danger", "danger"),
        ("success", "success"),
        ("primary", "primary"),
        ("info", "info"),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.CharField(max_length=250, blank=True)
    price = models.FloatField()
    pieces = models.IntegerField(null=True, blank=True)
    instructions = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="images/")
    labels = models.CharField(max_length=25, choices=LABELS, blank=True)
    label_colour = models.CharField(max_length=15, choices=LABEL_COLOUR, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:dishes", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("main:add-to-cart", kwargs={"slug": self.slug})

    def get_item_delete_url(self):
        return reverse("main:item-delete", kwargs={"slug": self.slug})

    def get_update_item_url(self):
        return reverse("main:item-update", kwargs={"slug": self.slug})


class Reviews(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True)
    review = models.TextField()
    posted_on = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.review


class CartItems(BaseModel):
    ORDER_STATUS = (("active", "Active"), ("delivered", "Delivered"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    ordered_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default="Active")
    delivery_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return self.item.title

    def get_remove_from_cart_url(self):
        return reverse("main:remove-from-cart", kwargs={"pk": self.pk})

    def update_status_url(self):
        return reverse("main:update_status", kwargs={"pk": self.pk})
