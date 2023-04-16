from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views import generic
from content.models import Course 
from .forms import ProductForm, CategoryForm, TechnologyForm, CountryForm, LanguageForm, ButtonForm
from .mixins import StaffUserMixin


class StaffView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/staff.html'
    queryset = Course.objects.all()
    paginate_by = 20
 


class ProductListView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/product_list.html'
    queryset = Course.objects.all()
    paginate_by = 10
    context_object_name = 'courses'


class CategoryCreateView(LoginRequiredMixin, StaffUserMixin, generic.CreateView):
    template_name = 'staff/category_create.html'
    form_class = CategoryForm

    def get_success_url(self):
        return reverse("staff:product-list")

    def form_valid(self, form):
        form.save()
        return super(CategoryCreateView, self).form_valid(form)


class TechnologyCreateView(LoginRequiredMixin, StaffUserMixin, generic.CreateView):
    template_name = 'staff/technology_create.html'
    form_class = TechnologyForm

    def get_success_url(self):
        return reverse("staff:product-list")

    def form_valid(self, form):
        form.save()
        return super(TechnologyCreateView, self).form_valid(form)


class CountryCreateView(LoginRequiredMixin, StaffUserMixin, generic.CreateView):
    template_name = 'staff/country_create.html'
    form_class = CountryForm

    def get_success_url(self):
        return reverse("staff:product-list")

    def form_valid(self, form):
        form.save()
        return super(CountryCreateView, self).form_valid(form)


class LanguageCreateView(LoginRequiredMixin, StaffUserMixin, generic.CreateView):
    template_name = 'staff/language_create.html'
    form_class = LanguageForm

    def get_success_url(self):
        return reverse("staff:product-list")

    def form_valid(self, form):
        form.save()
        return super(LanguageCreateView, self).form_valid(form)



class ButtonCreateView(LoginRequiredMixin, StaffUserMixin, generic.CreateView):
    template_name = 'staff/button_create.html'
    form_class = ButtonForm

    def get_success_url(self):
        return reverse("staff:product-list")

    def form_valid(self, form):
        form.save()
        return super(ButtonCreateView, self).form_valid(form)


class ProductCreateView(LoginRequiredMixin, StaffUserMixin, generic.CreateView):
    template_name = 'staff/product_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse("staff:product-list")

    def form_valid(self, form):
        form.save()
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(LoginRequiredMixin, StaffUserMixin, generic.UpdateView):
    template_name = 'staff/product_create.html'
    form_class = ProductForm
    queryset = Course.objects.all()

    def get_success_url(self):
        return reverse("staff:product-list")

    def form_valid(self, form):
        form.save()
        return super(ProductUpdateView, self).form_valid(form)


class ProductDeleteView(LoginRequiredMixin, StaffUserMixin, generic.DeleteView):
    template_name = 'staff/product_delete.html'
    queryset = Course.objects.all()

    def get_success_url(self):
        return reverse("staff:product-list")
