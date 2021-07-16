from numerology.models import ActivityTracking
from django.db import models

from django.utils.translation import gettext as _

class Book(ActivityTracking):
    title = models.CharField(max_length=30, blank=True, null=False)
    author = models.CharField(max_length=50, blank=True, null=False)
    price = models.IntegerField(default=0, blank=True, null=False)
    pages = models.IntegerField(default=0, blank=True, null=False)
    published_date = models.DateField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books', null=True, blank=True,verbose_name=_("book image"))
    description = models.TextField(blank=True,null=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-created_at"]


class Category(ActivityTracking):
    category = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return "{}".format(self.category)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
