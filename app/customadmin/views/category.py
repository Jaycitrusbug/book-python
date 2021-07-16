# -*- coding: utf-8 -*-
from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUpdateView,
    MyDetailView,
)
from django.db.models import Q
from django.shortcuts import render
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin

from django.shortcuts import reverse

from ..forms.category import CategoryCreationForm, CategoryChangeForm
from ..models import  Category


# -----------------------------------------------------------------------------
# Testimonials
# -----------------------------------------------------------------------------
class CategoryDetailView(MyDetailView):
    template_name = "customadmin/category/category_detail.html"
    context = {}

    def get(self,request,pk):
        self.context['category'] = Category.objects.filter(pk=pk).first()
        return render(request,self.template_name,self.context)

class CategoryListView(MyListView):

    ordering = ["id"]
    model = Category
    queryset = model.objects.all()
    template_name = "customadmin/category/category_list.html"



class CategoryCreateView(MyCreateView):
    """View to create Testimonial"""

    model = Category
    form_class = CategoryCreationForm
    template_name = "customadmin/category/category_form.html"


    def get_success_url(self):
        return reverse("customadmin:category-list")

class CategoryUpdateView(MyUpdateView):
    """View to update Testimonial"""

    model = Category
    form_class = CategoryChangeForm
    template_name = "customadmin/category/category_form.html"

    def get_success_url(self):
        return reverse("customadmin:category-list")

class CategoryDeleteView(MyDeleteView):
    """View to delete Testimonial"""

    model = Category
    template_name = "customadmin/confirm_delete.html"


    def get_success_url(self):
        return reverse("customadmin:category-list")


class CategoryAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Category
    queryset = Category.objects.all().order_by("created_at")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        # ctx.update({"obj": obj})
        # print(ctx)
        return t.render({"o": obj})

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(category=self.search)

            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {

                    "category": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data

















