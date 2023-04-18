from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, reverse, redirect, render
from .models import Course, Video, OrderItem, Category, Technology, Country,Language, Button
from .mixins import CoursePermissionMixin
from django.core.mail import send_mail
from .forms import AddToCartForm
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext as _
from .utils import get_or_set_order_session
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def is_valid_queryparam(param):
    return param != '' and param is not None

# class CourseListView(generic.ListView):
#     template_name = "content/course_list.html"
#     # queryset = Course.objects.all()

#     def get_queryset(self):
#         qs = Course.objects.all()
#         category = self.request.GET.get('category', None)
#         if category:
#             qs = qs.filter(Q(primary_category__name=category) |
#                            Q(secondary_categories__name=category)).distinct()
#         return qs

#     def get_context_data(self, **kwargs):
#         context = super(CourseListView, self).get_context_data(**kwargs)
#         context.update({
#             "categories": Category.objects.values("name")
#         })
#         return context


def CourseListView(request):
    qs = Course.objects.all()
    product_count = qs.count()
    

    categories = Category.objects.all()
    technologies = Technology.objects.all()
    countries = Country.objects.all()
    languages = Language.objects.all()
    buttons = Button.objects.all()
    
    category = request.GET.get('category')
    technology = request.GET.get('technology')
    country = request.GET.get('country')
    language = request.GET.get('language')
    button = request.GET.get('button')
    aliexpress_price_min = request.GET.get('aliexpress_price_min')
    aliexpress_price_max = request.GET.get('aliexpress_price_max')
    likes_count_min = request.GET.get('likes_count_min')
    likes_count_max = request.GET.get('likes_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    is_faceBook = request.GET.get('is_faceBook')
    is_pinterest = request.GET.get('is_pinterest')
    is_tiktok = request.GET.get('is_tiktok')
    has_video = request.GET.get('has_video')
    has_photo = request.GET.get('has_photo')
    

    if is_valid_queryparam(category) and category != 'All categories':
        qs = qs.filter(categories__name=category)

    if is_valid_queryparam(technology) and technology != 'Site type':
        qs = qs.filter(technologies__name=technology)

    if is_valid_queryparam(country) and country != 'Country':
        qs = qs.filter(countries__name=country)

    if is_valid_queryparam(language) and language != 'Language':
        qs = qs.filter(languages__name=language)

    if is_valid_queryparam(button) and button != 'Button':
        qs = qs.filter(buttons__name=button)

    if is_valid_queryparam(aliexpress_price_min):
        qs = qs.filter(aliexpress_price__gte=aliexpress_price_min)

    if is_valid_queryparam(aliexpress_price_max):
        qs = qs.filter(aliexpress_price__lt=aliexpress_price_max)

    if is_valid_queryparam(likes_count_min):
        qs = qs.filter(likes__gte=likes_count_min)

    if is_valid_queryparam(likes_count_max):
        qs = qs.filter(likes__lt=likes_count_max)

    if is_valid_queryparam(date_min):
        qs = qs.filter(ads_run_since__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(ads_run_since__lt=date_max)

    if is_faceBook == 'on':
        qs = qs.filter(is_faceBook=True)

    if is_pinterest == 'on':
        qs = qs.filter(is_pinterest=True)

    if is_tiktok == 'on':
        qs = qs.filter(is_tiktok=True)

    if has_video == 'on':
        qs = qs.filter(has_video=True)

    if has_photo == 'on':
        qs = qs.filter(has_photo=True)

    page_num = request.GET.get('page', 1)

    paginator = Paginator(qs, 4) # 6 employees per page


    try:
        qs = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        qs = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        qs = paginator.page(paginator.num_pages)

    context = {
        'queryset': qs,
        'categories': categories,
        'technologies': technologies,
        'countries': countries,
        'buttons': buttons,
        'languages': languages,
        'product_count': product_count,
    }
    return render(request, "content/course_list.html", context)



class CourseDetailView(generic.FormView):
    template_name = "content/course_detail.html"
    form_class = AddToCartForm


    def get_object(self):
            return get_object_or_404(Course, slug=self.kwargs["slug"])

    def get_success_url(self):
        return reverse("content:saved-product")
 
    
    


    def get_form_kwargs(self):
        kwargs = super(CourseDetailView, self).get_form_kwargs()
        kwargs["course_id"] = self.get_object().id
        return kwargs

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        course = self.get_object()

        item_filter = order.items.filter(
            course=course
         )

        if item_filter.exists():
            item = item_filter.first()
            item.quantity += int(form.cleaned_data['quantity'])
            item.save()

        else:
            new_item = form.save(commit=False)
            new_item.course = course
            new_item.order = order
            new_item.save()

        return super(CourseDetailView, self).form_valid(form)
   

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['course'] = self.get_object()
        return context


class VideoDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "content/video_detail.html"

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        course = self.get_course()
        subscription = self.request.user.subscription
        pricing_tier = subscription.pricing
        context.update({
            "has_permission": pricing_tier in course.pricing_tiers.all()
        })
        return context

    def get_course(self):
        return get_object_or_404(Course, slug=self.kwargs["slug"])

    def get_object(self):
        video = get_object_or_404(Video, slug=self.kwargs["video_slug"])
        return video

    def get_queryset(self):
        course = self.get_course()
        return course.videos.all()


class SavedProductView(generic.TemplateView):
    template_name = "content/saved_product.html"

    def get_context_data(self, **kwargs):
        context = super(SavedProductView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        return context


class RemoveFromSavedView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.delete()
        return redirect("content:saved-product")