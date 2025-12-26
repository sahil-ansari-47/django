from django.shortcuts import render
from django.contrib import messages
from .models import Services
from .forms import BookingForm
from django.views.generic import TemplateView, ListView, FormView, DetailView
    
class HomeView(TemplateView):
    template_name = 'main.html'

class ServicesView(ListView):
    model = Services
    context_object_name = 'services_list'
    template_name = 'services.html'
    paginate_by = 10

    def get_queryset(self):
        return Services.objects.all().order_by('-name')

class ServiceDetailView(DetailView):
    model = Services
    template_name = 'service_detail.html'
    context_object_name = 'service'

class BookingView(FormView):
    form_class = BookingForm
    success_url = '/booking/'
    template_name = 'booking.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Booking Confirmed!')
        return super().form_valid(form)

    
class AboutView(TemplateView):
    template_name = 'about.html'
