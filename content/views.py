from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, reverse, redirect, render
from .models import Course, Video, OrderItem
from .mixins import CoursePermissionMixin
from django.core.mail import send_mail
from .forms import ContactForm, AddToCartForm
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext as _
from .utils import get_or_set_order_session
from django.urls import reverse_lazy


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'pages/contact.html'

    def get_success_url(self):
        return reverse("content:course-list")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message.")
        name = form.cleaned_data.get(_('name'))
        email = form.cleaned_data.get(_('email'))
        message = form.cleaned_data.get(_('message'))

        full_message = f"""
            Received message below from {name}, {email}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)



class CourseListView(generic.ListView):
    template_name = "content/course_list.html"
    queryset = Course.objects.all()


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