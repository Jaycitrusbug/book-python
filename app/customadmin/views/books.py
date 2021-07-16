    # -*- coding: utf-8 -*-


from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin
from django.shortcuts import render

from django.shortcuts import reverse

from ..mixins import HasPermissionsMixin
from .generic import MyListView, MyCreateView, MyUpdateView, MyDeleteView, MyLoginRequiredView, MyDetailView
from ..forms.books import BookCreationForm, BookChangeForm
from ..models import Book

# -----------------------------------------------------------------------------
# Testimonials
# -----------------------------------------------------------------------------

class BookDetailView(MyDetailView):
    template_name = "customadmin/book/book_detail.html"
    context = {}

    def get(self,request, pk):
        self.context['books'] = Book.objects.filter(pk=pk).first()
        return render(request,self.template_name,self.context)


class BookListView(MyListView):
    ordering = ["id"]
    model = Book
    template_name = "customadmin/book/book_list.html"

class BookCreateView(MyCreateView):
    """View to create Testimonial"""

    model = Book
    form_class = BookCreationForm
    template_name = "customadmin/book/book_form.html"


    def get_success_url(self):
        return reverse("customadmin:book-list")

class BookUpdateView(MyUpdateView):


    model = Book
    form_class = BookChangeForm
    template_name = "customadmin/book/book_form.html"

    def get_success_url(self):
        return reverse("customadmin:book-list")

class BookDeleteView(MyDeleteView):
    """View to delete Testimonial"""

    model = Book
    template_name = "customadmin/confirm_delete.html"


    def get_success_url(self):
        return reverse("customadmin:book-list")

class BookAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Book
    queryset = Book.objects.all().order_by("created_at")

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
                Q(title__icontains=self.search)
                | Q(author__icontains=self.search)
                | Q(category__icontains=self.search)
                 | Q(price__icontains=self.search)
                 | Q(page__icontains=self.search)
                | Q(description__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                    "first_name": o.first_name,
                    "last_name": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data

















