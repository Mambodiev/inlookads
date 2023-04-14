from django.shortcuts import render
from .forms import ContactForm
from django.views import generic
from .models import Privacy, Terms, Faq, Price, About, Affiliate
from django.shortcuts import get_object_or_404

# def privacy(request):
#     qs = Privacy.objects.all()

#     context = {
#         'queryset': qs
#     }
#     return render(request, 'pages/privacy.html', context=context)


def home(request):

    context = {
        
    }
    return render(request, 'pages/home.html', context=context)



def privacy(request):
    privacy = Privacy.objects.get(pk=1)
   
    context={'privacy':privacy}
    return render(request,'pages/privacy.html', context)



def terms(request):
    terms = Terms.objects.get(pk=1)
   
    context={'terms':terms}
    return render(request,'pages/terms.html', context)



def faq(request):
    faq = Faq.objects.get(pk=1)
   
    context={'faq':faq}
    return render(request,'pages/faq.html', context)


def price(request):
    price = Price.objects.get(pk=1)
   
    context={'price':price}
    return render(request,'pages/price.html', context)



def about(request):
    about = About.objects.get(pk=1)
   
    context={'about':about}
    return render(request,'pages/about.html', context)



def blog(request):
    # blog = Blog.objects.get(pk=1)
   
    context={}
    return render(request,'pages/blog.html', context)


def affiliate(request):
    affiliate = Affiliate.objects.get(pk=1)
   
    context={'affiliate':affiliate}
    return render(request,'pages/affiliate.html', context)


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'pages/contact.html'

    def get_success_url(self):
        return reverse("content:course-list")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message.")
        # name = form.cleaned_data.get(_('name'))
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