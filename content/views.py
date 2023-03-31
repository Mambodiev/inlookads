from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, Video
from .mixins import CoursePermissionMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, reverse
from .forms import ContactForm 
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext as _


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


class CourseDetailView(generic.DetailView):
    template_name = "content/course_detail.html"
    queryset = Course.objects.all()


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