from django.db import models
from django.conf import settings

ELECTRONICS = "ELECTRONICS"
BOOKS = "BOOKS"
COMPUTERS = "COMPUTERS"

CATEGORY_CHOICES = (
    (ELECTRONICS, ELECTRONICS),
    (BOOKS, BOOKS),
    (COMPUTERS, COMPUTERS),
)

class Product(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product",
        null=True,
    )
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES,
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False, default=0.0
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
